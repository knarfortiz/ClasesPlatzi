# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# forms
from aplications.posts.forms import PostForm

# Utilities
from datetime import datetime

# Models
# from .exampleModels import posts
from .models import Post

class PostFeedView(LoginRequiredMixin, ListView):
    """ feed de post """
    template_name = 'posts/feed.html' 
    model = Post
    ordering = ('-created')
    paginate_by = 10
    context_object_name = 'posts'

    
class PostDetailView(LoginRequiredMixin, DetailView):
    """ detalle de post """
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'
    
class CreatePostView(LoginRequiredMixin, CreateView):
    """ Crear post """
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """ agregar usuario y perfil al contexto """
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["profile"] = self.request.user.profile
        return context
 

# @login_required
# def create_post(request):
    # """ Crea un nuevo post """
    # if request.method == 'POST':
        # form = PostForm(request.POST, request.FILES)
        # if form.is_valid():
            # form.save()
            # return redirect('posts:feed')
    # else:
        # form = PostForm()

    # context = {
            # 'form': form,
            # 'user': request.user,
            # 'profile': request.user.profile,
    # }

    # return render(request, 'posts/new.html', context)

# @login_required
# def list_posts(request):
    # posts = Post.objects.all().order_by('-created')
    # context = {
            # 'posts': posts,
    # }
    # return render(request, 'posts/feed.html', context)
