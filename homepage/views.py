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
        'about_us_title': trans['about_us_title'],
        'about_us_paragraph_1': trans['about_us_paragraph_1'],
        'about_us_paragraph_2': trans['about_us_paragraph_2'],
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
            'about_us_title': _('One of the most popular resorts in Georgia'),
            'about_us_paragraph_1': _("Home to one of the world's finest naturally warm, healing sulfur waters, Nunisi has been renowned in the Borjomi-Kharagauli region since the 17th century. Since 1856, Nunisi Balneological Resort has been treating skin conditions and remains open today for those seeking relaxation in the heart of nature."),
            'about_us_paragraph_2': _("Nunisi Forest Hotel and Spa welcomes everyone to spend their days at one of Georgia's most beautiful resorts. With lush greenery, fresh air, healing waters, and natural nutrition, it offers the perfect setting for an ideal vacation."),
        }

    finally:
        # If you cannot activate, activate the current language
        activate(cur_language)
    # Return translations
    return translations
