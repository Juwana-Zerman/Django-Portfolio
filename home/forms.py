from django.forms import ModelForm
from django.forms import Textarea, EmailField, CharField, ImageField
from .models import Contact, Post
from django import forms
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'message']
        widgets = {
            "message": Textarea(attrs={
                "placeholder": "Send me a message"
            })
        }

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'author',
            'content',
            'status',
            'image',
            'published_date']
        widgets = {
            "title": Textarea(attrs={
                "placeholder": "Title"
            }),
            "slug": Textarea(attrs={
                "placeholder": "Slug"
            }),
            "author": Textarea(attrs={
                "placeholder": "Author"
            }),
            "content": Textarea(attrs={
                "placeholder": "Content"
            }),
            "status": Textarea(attrs={
                "placeholder": "Status"
            }),
            "image": Textarea(attrs={
                "placeholder": "Image"
            }),
            "published_date": Textarea(attrs={
                "placeholder": "Published Date"
            }),
        }