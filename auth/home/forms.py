from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class SignUp(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


class EditUserPrifoleForm(UserChangeForm):
    
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email',]
        labels={'email':'Email'}