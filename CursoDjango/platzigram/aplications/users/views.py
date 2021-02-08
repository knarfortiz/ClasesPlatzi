""" users views """
# django
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.urls import reverse_lazy, reverse

# Exceptions
from django.db.utils import IntegrityError

# models
from django.contrib.auth.models import User
from aplications.users.models import Profile
from aplications.posts.models import Post

# Forms
from aplications.users.forms import ProfileForm, SignupForm

# Create your views here.

class UserDetailsView(LoginRequiredMixin, DetailView):
    """ detalles del usuario """
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_objetc_name = 'user'

    def get_context_data(self, **kwargs):
        """ Agregar listado de posts del usuario al contexto """
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """ logout view """
    template_name = 'users/logout.html'


class SignupView(FormView):
    """ Vista formuario de crear ususario """
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ guardar formulario de registro """
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """ Actualizar perfil de usuario """
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """ retorna perfil de usuario """
        return self.request.user.profile

    def get_success_url(self):
        """ retorna a perfil de usuario """
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    """ login view """
    template_name = "users/login.html"

# @login_required
# def logout_view(request):
    # logout(request)
    # return redirect('users:login')

# def login_view(request):
    # if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
            # login(request, user)
            # return redirect('posts:feed')
        # else:
            # contex = {
                    # 'error': 'Invalid username or password',
            # }
            # return render(request, 'users/login.html', contex)
    # return render(request, 'users/login.html')

# def signup_view(request):
    # if request.method == 'POST':
        # form = SignupForm(request.POST)
        # if form.is_valid():
            # form.save()
            # return redirect('login')
    # else:
        # form = SignupForm()
        # contex = {
                # 'form': form,
        # }
        # return render(request, 'users/signup.html', contex)

# @login_required
# def update_view(request):
    # """ Update profile """
    # # Implementacion de formularios Django
    # profile = request.user.profile
    # user = request.user
    # if request.method == 'POST':
        # form = ProfileForm(request.POST, request.FILES)
        # if form.is_valid():
            # data = form.cleaned_data
            # profile.website = data['website']
            # profile.phone_number = data['phone_number']
            # profile.biography = data['biography']
            # profile.picture = data['picture']
            # profile.save()
            # url = reverse('users:detail', kwargs={'username': user.username})
            # return redirect(url)
    # else:
        # # data = {
                # # 'website': profile.website,
                # # 'biography': profile.biography,
                # # 'phone_number': profile.phone_number,
        # # }
        # # form = ProfileForm(data)
        # form = ProfileForm()

    # contex = {
            # 'profile': profile,
            # 'user': user,
            # 'form': form
    # }
    # return render(request, 'users/update_profile.html', contex)
