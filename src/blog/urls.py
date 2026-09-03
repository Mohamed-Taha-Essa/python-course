from django.urls import path
from .views import post_list  , post_detail ,post_create ,comment_create

app_name= 'blog'

urlpatterns = [
    path('posts/',post_list),
    path('posts/new/',post_create),
    path('posts/<int:id>/comments/', comment_create, name='comment_create'),
    path('posts/<slug:slug>/', post_detail ,name='post_detail')
]