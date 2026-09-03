# form for model
# create form fields
from django import forms
from .models import Post ,Comment

#forms.Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title' ,'body']




class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ['name' , 'body' ,'email']