from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path(r'blogs/<int:blogs_id>', views.detail, name="detail"),
    path(r'projects/<int:projects_id>', views.project_details, name="project_details"),
    path(r'signup', views.signup_form, name="sign_up"),
    path(r'hireme', views.hire_me, name="hire_me"),
]
