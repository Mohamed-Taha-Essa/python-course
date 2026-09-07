from django.urls import path
from .views import post_list  , post_detail ,post_create ,comment_create,post_share,post_update,post_delete

from .cbv_views import PostListView,PostDetailView ,PostDeleteView,PostCreateView,PostUpdateView

app_name= 'blog'
#blog:post_detail

urlpatterns = [
    # path('',post_list ,name='post_list'),
    # path('posts/new/',post_create),
    path('posts/<slug:slug>/comments/create', comment_create, name='comment_create'),
   

    # path('posts/<slug:slug>/', post_detail ,name='post_detail'),


    # #shar post
    path('posts/<slug:slug>/share/' , post_share , name='post_share'), 
    # #post update
    # path('posts/<slug:slug>/updat/' , post_update , name='post_update'), 
    # #post delte
    # path('posts/<slug:slug>/delete/' , post_delete , name='post_delete'), 



    #class based view urls

    path('cbv/posts/' ,PostListView.as_view() ,name='post_list'),
    path('cbv/posts/<int:pk>/' ,PostDetailView.as_view() ,name='post_detail'),



    path('cbv/posts/create' ,PostCreateView.as_view() ,name='post_create'),

    path('cbv/posts/<slug:slug>/update' ,PostUpdateView.as_view() ,name='post_update'),

    path('cbv/posts/<slug:slug>/delete' ,PostDeleteView.as_view() ,name='post_delete'),
]
