"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog_app.views import home, login_user, signup_user, vd1,vd, page_1, add_blog, edit_blog, delete_blog, delete_blog_1, delete_blog_confirm, edit_blog_1, edit_blog_2, edit_blog_submit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('/login', login_user, name='login_user'),
    path('/signup', signup_user, name='signup_user'),
    path('/page1', page_1, name='page_1'),
    path('view_data', vd, name='view_data'),
    path('/add_blog', add_blog, name='add_blog'),
    path('/view_blog_data', vd1, name='view_blog_data')
    ,path('page_2', edit_blog, name='edit_blog'),
    path('/delete_blog', delete_blog, name='delete_blog')
    ,path('/edit_blog_1/<str:value_1>', edit_blog_1, name='edit_blog_1'),
    path('edit_blog_2', edit_blog_2, name='edit_blog_2'),
    path('edit_blog_submit', edit_blog_submit, name='edit_blog_submit'),
    path('/delete_blog_1', delete_blog_1, name='delete_blog_1'),
    path('/delete_blog_confirm', delete_blog_confirm, name='delete_blog_confirm')
]
