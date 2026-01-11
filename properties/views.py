from django.shortcuts import render
from .models import Property
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import get_all_properties

# Create your views here.

def property_list(request):
    property_data = get_all_properties()
    return JsonResponse(property_data, safe=False)