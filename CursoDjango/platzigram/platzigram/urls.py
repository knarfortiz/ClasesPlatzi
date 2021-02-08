# django
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

#local
from platzigram import views as local_views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('helloworld/', local_views.hello_world, name='hello_world'),
    path('sorted/', local_views.list_sorted, name='sort'),
    path('user/<str:name>/<int:edad>', local_views.user, name='hi'),

    path('', include(('aplications.posts.urls', 'post'), namespace='posts')),
    path('users/', include(('aplications.users.urls', 'users'), namespace='users')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
