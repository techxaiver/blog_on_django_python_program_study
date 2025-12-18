import os
import django
from django.test import Client
from django.urls import reverse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')
django.setup()

from django.contrib.auth.models import User
from blogs.models import BlogPost


def test_blog():
    c = Client()
    
    # Create users
    user1 = User.objects.create_user(username='user1', password='password')
    user2 = User.objects.create_user(username='user2', password='password')

    # Login as user1
    c.login(username='user1', password='password')

    # Test index
    response = c.get(reverse('blogs:index'))
    print(f"Index status code: {response.status_code}")
    assert response.status_code == 200

    # Test new post
    response = c.post(reverse('blogs:new_post'), {'title': 'User1 Post', 'text': 'Content by user1'})
    print(f"New post status code: {response.status_code}")
    assert response.status_code == 302
    
    # Verify post created and owned by user1
    post = BlogPost.objects.get(title='User1 Post')
    assert post.owner == user1
    print("New post created successfully by user1.")

    # Test edit post (own post)
    response = c.post(reverse('blogs:edit_post', args=[post.id]), {'title': 'Edited User1 Post', 'text': 'Edited content'})
    print(f"Edit own post status code: {response.status_code}")
    assert response.status_code == 302
    post.refresh_from_db()
    assert post.title == 'Edited User1 Post'
    print("Own post edited successfully.")

    # Login as user2
    c.logout()
    c.login(username='user2', password='password')

    # Test edit post (other user's post)
    response = c.post(reverse('blogs:edit_post', args=[post.id]), {'title': 'Hacked Post', 'text': 'Hacked content'})
    print(f"Edit other post status code: {response.status_code}")
    assert response.status_code == 404
    post.refresh_from_db()
    assert post.title == 'Edited User1 Post' # Should not change
    print("Other user's post edit blocked successfully.")

    # Cleanup
    user1.delete()
    user2.delete()

if __name__ == '__main__':
    test_blog()

