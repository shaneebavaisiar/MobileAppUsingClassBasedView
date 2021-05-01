from django.forms import ModelForm
from .models import Brands,Mobile,Order,Cart
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BrandForm(ModelForm):
    class Meta:
        model=Brands
        fields='__all__'

class MobileForm(ModelForm):
    class Meta:
        model=Mobile
        fields='__all__'

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields='__all__'

class UserRegForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']