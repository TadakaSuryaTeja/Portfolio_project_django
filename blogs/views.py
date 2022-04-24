from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Blogs


# Create your views here.

def index(request):
    blogs = Blogs.objects
    return render(request, 'blogs/index.html', {'blogs': blogs})


def detail(request, blogs_id):
    blogs_details = get_object_or_404(Blogs, pk=blogs_id)
    return render(request, 'blogs/detail.html', {'blogs': blogs_details})
