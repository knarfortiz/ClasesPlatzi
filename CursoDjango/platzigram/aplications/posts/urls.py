""" urls de Post """
# Django
from django.urls import path

# local views
from aplications.posts import views

urlpatterns = [
    path(
        route='', 
        view=views.PostFeedView.as_view(), 
        name='feed'
    ),
    path(
        route='new/', 
        view=views.CreatePostView.as_view(), 
        name='create'
    ),
    path(
        route='detail/<int:pk>', 
        view=views.PostDetailView.as_view(), 
        name='detail'
    ),
]
