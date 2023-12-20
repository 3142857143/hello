from django.shortcuts import render, redirect
from .models import User, Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .classes import Yash

def home(request):
    return render(request, 'home.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        users = User.objects.all()
        for user in users:
            if user.email == email:
                if user.password == password:
                    request.session['user_id'] = user.username
                    return redirect('page_1')
        return render(request, 'login_user.html')

    else:
        return render(request, 'login_user.html')

def signup_user(request):
    if request.method == 'POST':
        value_1 = request.POST.get('username')
        value_2 = request.POST.get('email')
        value_3 = request.POST.get('password')
        user = User.objects.all()
        for users in user:
            if users.username == value_1:
                return render(request, 'signup.html', {'error': 'username exist'})
            elif users.email == value_2:
                return render(request, 'signup.html', {'error': 'email exist'})

        user = User()
        user.username = value_1
        user.email = value_2
        user.password = value_3
        user.save()
        request.session['user_id'] = value_1
        return redirect('page_1')
    else:
        return render(request, 'signup.html')
# Create your views here.

def page_1(request):
    if request.session['user_id'] == None:
        return redirect('login_user')
    return render(request, 'page_1.html')

def add_blog(request):
    if request.method == 'POST':
        if request.session['user_id'] == None:
            return render(request, 'error.html')
        username = request.session['user_id']
        value_1 = request.POST.get('title')
        value_2 = request.POST.get('blog')
        blog = Blog()
        blog.username = username
        blog.title = value_1
        blog.blog = value_2
        all_blogs = Blog.objects.all()
        id = 0
        for blog_one in all_blogs:
            id = blog_one.blog_id
        blog.blog_id = id+1
        blog.save()
        return redirect('page_1')
def edit_blog(request):
    if request.session['user_id'] == None:
        return render(request, 'page_2.html')
    else:
        list_1 = []
        user_id = request.session['user_id']
        users = Blog.objects.all()
        for user in users:
            if user.username == user_id:
                new_user = Yash()
                new_user.username = user.username
                new_user.title = user.title
                new_user.blog = user.blog
                new_user.blog_id = user.blog_id
                list_1.append(new_user)
        if len(list_1) == 0:
            return render(request, 'page_2.html', {'no_found': 'None'})
        return render(request, 'page_2.html', {'user': list_1})
def delete_blog(request):
    if request.session['user_id'] == None:
        return render(request, 'page_3.html')
    else:
        list_1 = []
        user_id = request.session['user_id']
        users = Blog.objects.all()
        for user in users:
            if user.username == user_id:
                new_user = Yash()
                new_user.username = user.username
                new_user.title = user.title
                new_user.blog = user.blog
                new_user.blog_id = user.blog_id
                list_1.append(new_user)
        if len(list_1) == 0:
            return render(request, 'page_3.html', {'no_found': 'None'})
        return render(request, 'page_3.html', {'user': list_1})
def delete_blog_1(request):
    if request.method == 'POST':
        id = request.POST['id']
        blogs = Blog.objects.get(blog_id=id)
        return render(request, 'delete_this.html', {'blogs': blogs})

def delete_blog_confirm(request):
    if request.method == 'POST':
        id = request.POST['id']
        blog = Blog.objects.get(blog_id=id)
        blog.delete()
        return redirect('page_1')
def vd1(request):
    blog = Blog.objects.all()
    return render(request,'vd1.html', {'users': blog})

def vd(request):
    user = User.objects.all()
    return render(request,'vd.html', {'users': user})

def edit_blog_1(request, value_1):
    blogs = Blog.objects.all()
    blog = Blog.objects.get(username='{}'.format(request.session['user_id']), title='{}'.format(value_1))
    return render(request, 'edit_blog.html', {'user': blog})
def edit_blog_2(request):
    if request.method != 'POST':
        return redirect('home')
    if request.POST['id']:
        blogs = Blog.objects.get(blog_id=request.POST['id'])
        return render(request, 'edit_blog.html', {'user': blogs})

def edit_blog_submit(request):
    if request.method == 'POST':
        id = request.POST['id']
        blog = request.POST['blog']
        blogs = Blog.objects.get(blog_id=id)
        blogs.blog = blog
        blogs.save()
        return redirect('page_1')
