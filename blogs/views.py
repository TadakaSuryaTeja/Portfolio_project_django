from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Blogs, Projects


# Create your views here.

def index(request):
    blogs = Blogs.objects
    projects = Projects.objects
    return render(request, 'blogs/index.html', {'blogs': blogs, 'projects': projects})


def detail(request, blogs_id):
    blogs_details = get_object_or_404(Blogs, pk=blogs_id)
    return render(request, 'blogs/detail.html', {'blogs': blogs_details})


def project_details(request, projects_id):
    projects_details = get_object_or_404(Projects, pk=projects_id)
    return render(request, 'blogs/projects.html', {'projects': projects_details})


def signup_form(request):
    return render(request, 'blogs/signup.html')
