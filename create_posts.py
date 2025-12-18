import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')
django.setup()

from blogs.models import BlogPost

BlogPost.objects.create(title='First Post', text='This is the first post.')
BlogPost.objects.create(title='Second Post', text='This is the second post.')
print('Posts created.')
