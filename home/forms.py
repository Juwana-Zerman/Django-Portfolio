from django.forms import ModelForm
from django.forms import Textarea, EmailField, CharField, ImageField
from .models import Contact, Post

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
            #'image',
            'published_date']



        