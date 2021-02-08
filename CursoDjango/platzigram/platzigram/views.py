# Utilities
from datetime import datetime
    
from django.http import (
        HttpResponse, JsonResponse
    )

 
def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(f'Hola la fecha actual es: {now}')

def list_sorted(request):
    #import pdb; pdb.set_trace()
    number = [int(i) for i in request.GET['number'].split(',')]
    numList = sorted(number, reverse=True)
    data = JsonResponse({
            'status': 'ok', 
            'numbers': numList,
            'message': 'Todo bien',
    })
    return HttpResponse(data, content_type='application/json')

def user(request, name, edad):

    if edad < 15:
        data = JsonResponse({
            'status': 'Error',
            'message': 'El usuario debe ser mayor de 15 años',
        })
    else:
        data = JsonResponse({
            'status' : 'ok',
            'user': {
                'nombre': name,
                'edad': edad,
            },
            'message': 'Usuario Correcto',
        })
    
    return HttpResponse(data, content_type='application/json')

    """TODO: Docstring for .
    :returns: TODO

    """
    pass 

def function(arg1):
    """TODO: Docstring for function.

    :arg1: TODO
    :returns: TODO

    """
    pass

