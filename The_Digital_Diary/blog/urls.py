from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.publish_post, name='publish_post'),
    path('ckeditor/', include('django_ckeditor_5.urls')),
]
