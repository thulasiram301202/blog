from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from .models import Post
from django.core.paginator import Paginator
from .forms import ContactForm

def index(request):
    blog_title = "Posts"
    all_posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'blog_title': blog_title, 'page_obj': page_obj})

def detail(request, slug):
    try: 
        post = Post.objects.get(slug=slug)
        related_post = Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post Doesn't Exist!")
    return render(request, 'detail.html', {'post': post, 'related_post': related_post})

def old_url_redirect(request):
    return redirect(reverse('new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL")

def contact_view(request):
    logger = logging.getLogger("Testing")
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            logger.debug(f"POST Data is {name} {email} {message}")
            success_message = "Your email has been sent successfully"
            form = ContactForm()  # Reset the form to be empty
            return render(request, 'contact.html', {'form': form, 'success_message': success_message})
        else:
            logger.debug("Form Validation Failure")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def about_view(request):
    return render(request, 'about.html')


