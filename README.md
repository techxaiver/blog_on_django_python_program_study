# Blog Project

这是一个基于 Django 框架开发的简单博客系统。用户可以注册账户，登录系统，并发布或编辑自己的博客文章。

## 功能特性

*   **用户认证系统**
    *   用户注册
    *   用户登录/注销
*   **博客管理**
    *   浏览博客文章列表
    *   发布新文章
    *   编辑已发布的文章
    *   文章包含标题、内容、发布时间和作者信息

## 技术栈

*   Python
*   Django
*   SQLite (默认数据库)

## 安装与运行

1.  **克隆项目**

    ```bash
    git clone https://github.com/techxaiver/blog_on_django_python_program_study.git
    cd Blog
    ```

2.  **设置虚拟环境**

    项目包含一个名为 `ll_env` 的虚拟环境配置。你需要激活它或创建一个新的虚拟环境。

    *   Windows:
        ```bash
        .\ll_env\Scripts\activate
        ```
    *   Linux/macOS:
        ```bash
        source ll_env/bin/activate
        ```

3.  **安装依赖**

    确保安装了 Django：
    ```bash
    pip install django
    ```

4.  **数据库迁移**

    ```bash
    python manage.py migrate
    ```

5.  **运行开发服务器**

    ```bash
    python manage.py runserver
    ```

    访问 `http://127.0.0.1:8000/` 查看应用。

## 辅助脚本

项目根目录下包含一些用于快速初始化的辅助脚本：

*   **`create_superuser.py`**
    *   用于快速创建一个默认的超级用户。
    *   默认账号: `admin`
    *   默认密码: `password`
    *   运行方式: `python create_superuser.py`

*   **`create_posts.py`**
    *   用于生成一些测试用的博客文章数据。
    *   运行方式: `python create_posts.py`

## 项目结构

*   `Blog/`: 项目的配置文件 (settings, urls, etc.)
*   `blogs/`: 博客应用的主要逻辑 (models, views, templates)
*   `users/`: 用户认证应用 (login, register)
*   `templates/`: HTML 模板文件
