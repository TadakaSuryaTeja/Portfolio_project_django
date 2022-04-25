from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('<int:blogs_id>', views.detail, name="detail"),
    path('<int:projects_id>', views.detail, name="detail"),

]
