from django.db import models

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

# class User(models.Model):
   # email = models.EmailField(unique=True)
   # password = models.CharField(max_length=100)
   # first_name = models.CharField(max_length=100)
   # last_name = models.CharField(max_length=100)
   # is_admin = models.BooleanField(default=False)
   # bio = models.TextField(blank=True)
   # birthday = models.DateField(blank=True, null=True)
   # created = models.DateTimeField(auto_now_add=True)
   # modified = models.DateTimeField(auto_now=True)

   # def __str__(self):
       # return self.email

