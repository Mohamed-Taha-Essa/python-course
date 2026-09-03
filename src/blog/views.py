from django.shortcuts import render ,redirect
from .models import Post
from django.shortcuts import get_object_or_404
from datetime import date
from .forms import PostForm ,CommentForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage
# Create your views here.

def post_list(request):
    
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts ,5)
    page_number =request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request ,'blog/post_list.html', {'posts': posts})





def post_detail(request, slug):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     post = None
    #     return render(request, 'blog/post_not_found.html', {})

    post = get_object_or_404(Post,slug=slug)
    return render(request ,'blog/post_detail.html', {'post' : post})

def post_create(request):
    author = User.objects.all()[1]
    print(author.username)
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print('form is valid')
            post =form.save(commit=False)
            post.author = author
          
            post.save()
            print('post is created')

            return redirect('blog:post_detail', id=post.id)
        else :
            print('form is not valid')
    else:
        form = PostForm()
    return render(request ,'blog/post_form.html' ,{'form':form})

def comment_create(request ,id):
    post = Post.objects.get(id=id)
    
    if request.method =='POST':
        form =CommentForm(request.POST)
        if form.is_valid():
            print('form is valid')
            comment =form.save(commit=False)
            comment.post = post
          
            comment.save()
            print('comment is created')

            return redirect('blog:post_detail', id=post.id)
        else :
            print('form is not valid')
    else:
        form = CommentForm()
    return render(request ,'blog/comment_form.html' ,{'form':form})

# def post_list(request):
    # posts = Post.objects.all()
    # posts = Post.objects.filter(status='draft').order_by('-publish')
    #queryset on date and time
    # posts = Post.objects.filter(title='python')
    # posts = Post.objects.filter(publish__date=date(2026,8,31))
    # posts = Post.objects.filter(publish__year=2026)
    # posts = Post.objects.filter(publish__month=8)
    # posts = Post.objects.filter(publish__day=30)
    # posts = Post.objects.filter(publish__date__gt=date(2026,8,31))
    # posts = Post.objects.filter(publish__date__gte=date(2026,8,31))
    
    
    #query on relationship (author) lookup
    
    # posts = Post.objects.filter(author__username ='admin')
    # posts = Post.objects.filter(author__username__startswith ='ad')
    # posts = Post.objects.filter(author__username__startswith ='ad' ,publish__date__gte=date(2026,8,31))
    # posts = Post.objects.filter(author__username__startswith ='ad').filter(publish__date__gte=date(2026,8,31))
    # posts = Post.objects.filter(author__username__contains ='ch')
    
    #lookup on title
    
    # posts = Post.objects.filter(title__exact ='python')
    # posts = Post.objects.filter(title__iexact ='python')
    
    #    #lookup on id
    
    # posts = Post.objects.filter(id__in=[1, 5,4,2,8,9,17] )
    # posts = Post.objects.filter(id__gt=9 )
    # posts = Post.objects.filter(id__gte=9 )
    # posts = Post.objects.filter(id__lt=9 )
    # posts = Post.objects.filter(id__lte=9 )


    #exclude
    # posts = Post.objects.filter(publish__year=2026).exclude(author__username__startswith='ad')


    #ordering 
    # posts = Post.objects.filter(publish__year=2026).order_by('title') #ascendin A-Z
    # posts = Post.objects.filter(publish__year=2026).order_by('-title') #descendin z-a
    # posts = Post.objects.order_by('-publish' )
    # posts = Post.objects.order_by('-publish' ).order_by('title')
    # posts = Post.objects.order_by('?') #random
   
   #slicing
    # posts = Post.objects.all()[:6] 
    # posts = Post.objects.all()
    

    # return render(request ,'blog/post_list.html', {'posts': posts})
