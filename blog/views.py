from django.shortcuts import render,get_object_or_404
from .models import Blog

def showBlogs(request):
    blogs=Blog.objects
    return render(request,'blog/Blogs.html',{'blogs':blogs})

def detail(request,blog_id):
    blogDetail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/Details.html',{'blog':blogDetail})
