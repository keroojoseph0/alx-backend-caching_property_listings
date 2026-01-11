from django.contrib import admin
from .models import Property
from properties.models import Property

# Register your models here.

admin.site.register(Property)
