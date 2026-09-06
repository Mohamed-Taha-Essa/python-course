from django.urls import path
from .views import post_list  , post_detail ,post_create ,comment_create,post_share

app_name= 'blog'
#blog:post_detail

urlpatterns = [
    path('posts/',post_list),
    path('posts/new/',post_create),
    path('posts/<int:id>/comments/', comment_create, name='comment_create'),
   

    path('posts/<slug:slug>/', post_detail ,name='post_detail'),


    #shar post
    path('posts/<slug:slug>/share/' , post_share , name='post_share')
]