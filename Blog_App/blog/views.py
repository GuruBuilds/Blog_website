from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.

def index(request):
    """View function for the home page of the site."""
    # Render the HTML template index.html with the data in the context variable
    blogs = Blog.objects.all()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            return redirect('index')
    else:
        form = BlogForm()

    return render(request, 'blog/index.html', {'blogs': blogs, 'form': form})