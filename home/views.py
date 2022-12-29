from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from .forms import ContactForm, PostForm
from .models import Post
from django.views.generic import DetailView
from django.views.generic import ListView
from django.utils import timezone


# from django.core.mail import send_mail, BadHeaderError, EmailMessage

# Create your views here.
def home(request):
    return render(request, 'home.html')

class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("thanks")


def thanks(request):
    return HttpResponse("Thank you! Will get in touch soon.")


def contact(request):
    if request.method=="POST":
        # form = ContactForm(data=request.POST)
        # if form.is_valid():
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        #print(name, email, message)
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        print("The data has been written to the db")

        # Email the profile with the contact information
    #         send_mail(name, message, email, ['testmail@gmail.com'], fail_silently=False)

        #return HttpResponseRedirect('/contact')
    # else:
    #     form = ContactForm()


    return render(request, 'contact.html')


class PostList(ListView):
    ordering = ['-created_on']
    template_name = 'blog.html'
    context_object_name = 'posts'
    model = Post

class PostDetail(DetailView):
    model = Post
    ordering = ['created_on']
    template_name = 'post-detail.html' #'post_detail.html'

def time_function(request):
    # get the object
    object = Object.objects.get(id=1)

    # create date and time objects with current time zone
    date_time_now = datetime.now(timezone.utc)

    # assign time to object field
    object.created_on = date_time_now
    object.save()


# class AddPost(CreateView):
#     model = Post
#     template_name = 'add_post.html'
#     fields = '__all__'
