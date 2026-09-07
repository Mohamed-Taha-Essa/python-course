from django.shortcuts import render ,redirect
from .models import Post
# def post_list(request):
    
#     posts = Post.objects.all() ------------>       query
   
#     context = {'posts': posts}       ------->       context 
#     return render(request ,'blog/post_list.html',context ) --->template


from django.views.generic import ListView ,DetailView,UpdateView,CreateView ,DeleteView
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
class PostListView(ListView):
    model =Post     #(object_list)    model_name_list(post_list)
    # template_name= 'blog/post_list.html' #name_of_app/model_name_list.html
    # context_object_name='posts'
    paginate_by=5


    # def get_queryset(self):
    #     return Post.objects.filter(author__username='admin')

    def get_queryset(self):
        queryset = Post.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query)


        return queryset




class PostDetailView(DetailView):
    model =Post  #(object_name)


class PostDeleteView(DeleteView):
    model=Post
    template_name ="blog/post_confirm_delete.html"
    success_url = reverse_lazy('blog:post_list')
    context_object_name ='post'

class PostCreateView(CreateView):
    model =Post
    form_class =PostForm
    template_name ='blog/post_form.html'

    def form_valid(self, form):
        # form.instance.author = self.request.user
        author = User.objects.all()[1]
        form.instance.author = author
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
