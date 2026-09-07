# form for model
# create form fields
from django import forms
from .models import Post ,Comment




#forms.Form
# class EmailPostForm(forms.Form):
#     name = forms.CharField(max_length=40)
#     email = forms.EmailField() #sender email
   
#     to = forms.EmailField()  #receiver email
#     comments= forms.CharField(required= False ,widget=forms.Textarea)
# forms.py

from django import forms


class EmailPostForm(forms.Form):

    name = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your name",
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email",
            }
        )
    )

    to = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Recipient email",
            }
        )
    )

    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Write a message...",
                "rows": 5,
            }
        )
    )

#forms.modelform
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title' ,'body' ]




class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields = ['name' , 'body' ,'email']