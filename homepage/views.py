from django.shortcuts import render
from django.conf import settings


def index(request):
    '''Return the homepage'''
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(
        request,
        'homepage/index.html',
        context
    )
