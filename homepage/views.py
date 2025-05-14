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
        'header_link_about_us': trans['header_link_about_us'],
        'header_link_nunisi_water': trans['header_link_nunisi_water'],
        'hotel_name': trans['hotel_name'],
        'welcome_message': trans['welcome_message'],
        'booking_title': trans['booking_title'],
        'booking_email': trans['booking_email'],
        'booking_phone': trans['booking_phone'],
        'booking_or': trans['booking_or'],
        'booking_booking_com': trans['booking_booking_com'],
        'about_us_title': trans['about_us_title'],
        'about_us_paragraph_1': trans['about_us_paragraph_1'],
        'about_us_paragraph_2': trans['about_us_paragraph_2'],
        'water_title': trans['water_title'],
        'water_paragraph': trans['water_paragraph'],
        'spa_title': trans['spa_title'],
        'spa_paragraph_1': trans['spa_paragraph_1'],
        'spa_paragraph_2': trans['spa_paragraph_1'],
        'location_title': trans['location_title'],
        'location_paragraph': trans['location_paragraph'],
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
            'header_link_about_us': _('About Us'),
            'header_link_nunisi_water': _('Nunisi Water'),
            'hotel_name': _('Nunisi Forest Hotel and Spa'),
            'welcome_message': _('Where luxury is natural!'),
            'booking_title': _('Book now via'),
            'booking_email': _(' Email: nunisi2002@gmail.com'),
            'booking_phone': _(' Phone: (+995) 599 22 55 80'),
            'booking_or': _('or'),
            'booking_booking_com': _('Book through booking.com'),
            'about_us_title': _('One of the most popular resorts in Georgia'),
            'about_us_paragraph_1': _("Home to one of the world's finest naturally warm, healing sulfur waters, Nunisi has been renowned in the Borjomi-Kharagauli region since the 17th century. Since 1856, Nunisi Balneological Resort has been treating skin conditions and remains open today for those seeking relaxation in the heart of nature."),
            'about_us_paragraph_2': _("Nunisi Forest Hotel and Spa welcomes everyone to spend their days at one of Georgia's most beautiful resorts. With lush greenery, fresh air, healing waters, and natural nutrition, it offers the perfect setting for an ideal vacation."),
            'water_title': _('The Unique Waters of Nunisi Forest Hotel and Spa'),
            'water_paragraph': _("The secret behind Nunisi's healing power lies in its water. Rich in silicic acid, Nunisi's mineral waters are renowned for their therapeutic benefits. They aid in treating various skin conditions such as psoriasis, eczema, neurodermatitis, and impetigo, as well as bone, joint, and peripheral nervous system disorders. The primary treatment method involves mineral water baths, offering a natural path to wellness and relaxation."),
            'spa_title': _('Services'),
            'spa_paragraph_1': _('Since many guests visit Nunisi for health and wellness treatments, we offer a range of additional services to complement our mineral bath therapy. These include private doctor consultations, massage therapy, and other medical services designed to enhance relaxation and healing.'),
            'spa_paragraph_2': _('Doctor Consultations: Guests have the opportunity to receive personalized advice from a qualified doctor. Each consultation is tailored to the individual, ensuring the most appropriate treatment plan for their specific needs.'),
            'location_title': _('Location'),
            'location_paragraph': _('Situated 750 meters above sea level within the Borjomi-Kharagauli National Park, in the scenic gorge of the Nunisistskali River, lies the Nunisi Forest Hotel and Spa. With its unique combination of a mild climate and high-alkalinity mineral water, Nunisi is especially beneficial for individuals suffering from skin conditions.'),
        }

    finally:
        # If you cannot activate, activate the current language
        activate(cur_language)
    # Return translations
    return translations
