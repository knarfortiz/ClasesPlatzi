""" Users Forms """
from django import forms

# models
from .models import Profile
from django.forms import ModelForm
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    """ Sign up form . """
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=70, widget=forms.PasswordInput)
    password_conf = forms.CharField(max_length=70, widget=forms.PasswordInput)

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
            min_length=6,
            max_length=70,
            widget=forms.EmailInput()
    )

    def clean_username(self):
        """ valida que el usuario sea unico """
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El usuario ya está en uso')
        return username

    def clean(self):
        """ verificar la contraseña con la confirmacion """
        data = super().clean()
        password = data['password']
        password_conf = data['password_conf']

        if password != password_conf:
            raise forms.ValidationError('Las contraseñas son diferentes')
        return data

    def save(self):
        """ Crear un usuario y perfil """
        data = self.cleaned_data
        data.pop('password_conf')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()



class ProfileForm(forms.Form):
    """ Profile form """
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=True)
    
    # website.widget.attrs.update({'class': 'form-control'})
    # biography.widget.attrs.update({'class': 'form-control'})
    # phone_number.widget.attrs.update({'class': 'form-control'})
    # website.widget.attrs.update({'class': 'form-control'})

# class ProfileForm(ModelForm):
    # class Meta:
        # model = Profile
        # fields = [
                # 'website', 
                # 'biography',
                # 'phone_number',
                # 'picture'
        # ]
    
    
