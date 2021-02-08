""" urls de users """
# Django
from django.urls import path
from django.views.generic import TemplateView

# views
from aplications.users import views

urlpatterns = [
    path(
        route='logout/', 
        view=views.LoginView.as_view(), 
        name='logout'
    ),
    path(
        route='login/', 
        view=views.LoginView.as_view(), 
        name='login'
    ),
    path(
        route='signup/', 
        view=views.SignupView.as_view(), 
        name='signup'
    ),
    path(
        route='me/profile', 
        view=views.UpdateProfileView.as_view(), 
        name='update_profile'
    ),
    path(
        route='<str:username>/',
        view=views.UserDetailsView.as_view(),
        name='detail'
    ),
]
