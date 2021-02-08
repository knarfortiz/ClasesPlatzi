""" Platzigram middleware """
# Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """ Completar perfil middleware

    Se asegura que los perfiles esten completos (bio, picture)
    para poder usar la app """

    def __init__(self, get_response):
        """ Inicializar middleware """
        self.get_response = get_response

    def __call__(self, request):
        """ Codigo que se ejecuta antes de que la vista sea llamada """
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                        return redirect('users:update_profile')

        response = self.get_response(request)
        return response


