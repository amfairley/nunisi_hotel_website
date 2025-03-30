from django.shortcuts import render
from django.conf import settings
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext


def index(request):
    '''Return the homepage'''
    trans = translate(language=get_language() or settings.LANGUAGE_CODE)
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'DEBUG': settings.DEBUG,
        'hotel_name': trans['hotel_name'],
        'welcome_message': trans['welcome_message'],
    }
    return render(
        request,
        'homepage/index.html',
        context,
    )


def translate(language):
    '''Function to translate homepage text'''
    # get the current language
    cur_language = get_language()
    translations = {}  # Ensure it is defined even if activation failes
    # Try to activate the language you pass as a parameter
    try:
        activate(language)
        # Select and define translations
        translations = {
            'hotel_name': _('Nunisi Forest Hotel and Spa'),
            'welcome_message': _('Where luxury is natural!'),
        }

    finally:
        # If you cannot activate, activate the current language
        activate(cur_language)
    # Return translations
    return translations
