from django.contrib import admin

# Register your models here.
from .models import Mobile,Brands,Order,Cart
admin.site.register(Mobile)
admin.site.register(Brands)
admin.site.register(Order)
admin.site.register(Cart)
