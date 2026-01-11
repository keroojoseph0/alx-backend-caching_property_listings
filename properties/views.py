from django.shortcuts import render
from .models import Property
from django.views.decorators.cache import cache_page
from django.http import JsonResponse

# Create your views here.

@cache_page(60 * 15)
def property_list(request):
    data = list(Property.objects.values())

    return JsonResponse(data, safe=False)