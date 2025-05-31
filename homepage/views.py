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
        # Translations
        # Site Header/Footer
        'site_header_home': trans['site_header_home'],
        'site_header_water': trans['site_header_water'],
        'site_header_rooms': trans['site_header_rooms'],
        'site_header_photo': trans['site_header_photo'],
        'call_us': trans['call_us'],
        # Rest of the page
        # Header
        'header_link_about_us': trans['header_link_about_us'],
        'header_link_nunisi_water': trans['header_link_nunisi_water'],
        'header_link_services': trans['header_link_services'],
        'header_link_location': trans['header_link_location'],
        'header_link_reviews': trans['header_link_reviews'],
        # Hero Image
        'hotel_name': trans['hotel_name'],
        'welcome_message': trans['welcome_message'],
        # Booking
        'booking_title': trans['booking_title'],
        'booking_email': trans['booking_email'],
        'booking_phone': trans['booking_phone'],
        'booking_or': trans['booking_or'],
        'booking_through': trans['booking_through'],
        'booking_booking_com': trans['booking_booking_com'],
        'booking_rooms_button': trans['booking_rooms_button'],
        # About Us
        'about_us_carousel_prev': trans['about_us_carousel_prev'],
        'about_us_carousel_next': trans['about_us_carousel_next'],
        'about_us_title': trans['about_us_title'],
        'about_us_paragraph': trans['about_us_paragraph'],
        'about_us_legend': trans['about_us_legend'],
        'about_us_legend_text_1': trans['about_us_legend_text_1'],
        'about_us_legend_text_2': trans['about_us_legend_text_2'],
        # Water
        'water_title': trans['water_title'],
        'water_paragraph_1': trans['water_paragraph_1'],
        'water_paragraph_2': trans['water_paragraph_2'],
        'water_button': trans['water_button'],
        # Services
        'spa_title': trans['spa_title'],
        'services_paragraph': trans['services_paragraph'],
        # Packages
        'packages_title': trans['packages_title'],
        'packages_comment': trans['packages_comment'],
        'packages_medical_title': trans['packages_medical_title'],
        'packages_wellness_title': trans['packages_wellness_title'],
        'packages_esthetic_title': trans['packages_esthetic_title'],
        'packages_beauty_title': trans['packages_beauty_title'],
        'packages_family_title': trans['packages_family_title'],
        'packages_accomm_one_week': trans['packages_accomm_one_week'],
        'packages_accomm_five_days': trans['packages_accomm_five_days'],
        'packages_food': trans['packages_food'],
        'packages_diet_food': trans['packages_diet_food'],
        'packages_food_child': trans['packages_food_child'],
        'packages_derma': trans['packages_derma'],
        'packages_wellness': trans['packages_wellness'],
        'packages_mineral_pool_procedures': trans['packages_mineral_pool_procedures'],
        'packages_mineral_pool_access': trans['packages_mineral_pool_access'],
        'packages_skin': trans['packages_skin'],
        'packages_massage': trans['packages_massage'],
        'packages_facial_massage': trans['packages_facial_massage'],
        'packages_morning_exercise': trans['packages_morning_exercise'],
        'packages_morning_evening_exercise': trans['packages_morning_evening_exercise'],
        'packages_yoga': trans['packages_yoga'],
        'packages_hike': trans['packages_hike'],
        'packages_horse': trans['packages_horse'],
        'packages_fishing': trans['packages_fishing'],
        'packages_activities': trans['packages_activities'],
        # Location
        'location_title': trans['location_title'],
        'location_paragraph_1': trans['location_paragraph_1'],
        'location_paragraph_2': trans['location_paragraph_2'],
        'location_paragraph_3': trans['location_paragraph_3'],
        # Reviews
        'review_1_content': trans['review_1_content'],
        'review_1_name': trans['review_1_name'],
        'review_2_content': trans['review_2_content'],
        'review_2_name': trans['review_2_name'],
        'review_3_content': trans['review_3_content'],
        'review_3_name': trans['review_3_name'],
        'review_4_content': trans['review_4_content'],
        'review_4_name': trans['review_4_name'],
        'review_5_content': trans['review_5_content'],
        'review_5_name': trans['review_5_name'],
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
            # Site header and footer
            'site_header_home': _('Home'),
            'site_header_water': _('Nunisi Water'),
            'site_header_rooms': _('Build Your Stay'),
            'site_header_photo': _('Photo Gallery'),
            'call_us': _('Call us today on'),
            # Rest of the page
            # Header
            'header_link_about_us': _('About Us'),
            'header_link_nunisi_water': _('Nunisi Water'),
            'header_link_services': _('Services'),
            'header_link_location': _('Location'),
            'header_link_reviews': _('Reviews'),
            # Hero Image
            'hotel_name': _('Nunisi Forest Hotel and Spa'),
            'welcome_message': _('Where luxury is natural!'),
            # Booking
            'booking_title': _('Book now via'),
            'booking_email': _(' Email: '),
            'booking_phone': _(' Phone: (+995) 599 22 55 80'),
            'booking_through': _('Through '),
            'booking_or': _('or'),
            'booking_booking_com': _('Book through booking.com'),
            'booking_rooms_button': _('Take a look at our rooms & packages'),
            # About Us
            'about_us_carousel_prev': _('About Us'),
            'about_us_carousel_next': _('The Legend of Nunisi'),
            'about_us_title': _('A unique resort of world importance'),
            'about_us_paragraph': _("Nunisi mineral water was known as early as the 17th century. The balneological resort has been hosting those who want to relax in picturesque nature since 1856. It cures skin diseases and rehabilitates health in conditions of deep relaxation. Naturally warm, gas-filled water baths containing flint, sulfur, and other minerals achieve amazing healing results. Mixed forest, old trees, green surroundings, healing air, baths, and natural products are the best for deep relaxation and restoration of strength."),
            'about_us_legend': _('The Legend of Nunisi'),
            'about_us_legend_text_1': _('There is a legend about the discovery of Nunisi water, which is associated with the great Georgian king, David the Builder. The legend tells us that King David was returning from a battle. His horses, tired from walking, whose skin was peeling and sores were forming, they lay down in the Nunisi water and soon recovered. The overjoyed king made a large donation to the temple in the village. The Nunisi Monastery of the Nativity of the Virgin Mary, built in the 9th-10th centuries, is still in operation today.'),
            'about_us_legend_text_2': _('The healing use of Nunisi water has been known since the 9th century. The population noticed that their pets were being cured of malaise with the help of the mineral water, tried using it themselves and got results. Over time, the whole of Georgia learned about the healing properties of the springs. The water of Nunisi was called “a garment and a blessing” by the 18th-century Georgian geographer Vakhushti Batonishvili and is actively mentioned in his works.'),
            # Water
            'water_title': _('Indication of Nunisi healing water'),
            'water_paragraph_1': _(
                """Legends associated with Nunisi healing water are confirmed by modern scientific research and medical practice.
                Rehabilitation with healing water in Nunisi has become a symbol of a healthy lifestyle.
                Nunisi is a place where you can receive healing and wellness procedures using only natural means - spring water, in beautiful nature, in the middle of the forest, in a peaceful and ecologically clean environment.
                For this purpose, mineral water baths and showers are used, which are prescribed individually by the resort's dermatologist, depending on the patient's condition.

                Typical diseases of the resort:
                - Psoriasis
                - Atopic dermatitis (eczema)
                - Lichen planus
                - Prurigo
                - Seborrheic dermatitis
                - And others.
                """),
            'water_paragraph_2': _('You will also receive aesthetic therapy, with a noticeable skin rejuvenation effect in our hotel.'),
            'water_button': _("Learn more about Nunisi's water"),
            # Services
            'spa_title': _('Services'),
            'services_paragraph': _(
                """- Three meals a day are included in the room rate
                - The restaurant accepts individual orders
                - Doctor consultation 
                - Bath and Massage therapy 
                The hotel has an open bar (with billiards, film screenings). Excursions are organized to the monks' cave (so-called Noah's Ark), the Fathers' Monastery and the waterfall.
                The hotel has a 24-hour guarded parking lot. Guests are transported to the territory by their own cable car.
                The hotel has a laundry service. Pets are allowed by prior arrangement with the administration.
                """),
            # Packages
            'packages_title': _('Choose from one of our tailored experience packages'),
            'packages_comment': _('Or contact us to arrange a bespoke holiday.'),
            'packages_medical_title': _('Medical Package'),
            'packages_wellness_title': _('Wellness Recreational Package'),
            'packages_esthetic_title': _('Esthetic Retreat Package'),
            'packages_beauty_title': _('Beauty Restoration Package'),
            'packages_family_title': _('Family Package'),
            'packages_accomm_one_week': _('One week of hotel accommodation'),
            'packages_accomm_five_days': _('Five days of hotel accommodation'),
            'packages_food': _('Three meals a day'),
            'packages_diet_food': _('Three healthy meals a day'),
            'packages_food_child': _('Three meals a day including a child menu'),
            'packages_derma': _('Dermatologist consultation'),
            'packages_wellness': _('Wellness procedure of 2 showers and 10 baths'),
            'packages_mineral_pool_procedures': _('10 procedures in a mineral water pool'),
            'packages_mineral_pool_access': _('Access to the mineral pool'),
            'packages_skin': _('Nunisi water procedures for skin rejuvenation and anti-aging'),
            'packages_massage': _('Massage'),
            'packages_facial_massage': _('Facial massage'),
            'packages_morning_exercise': _('Morning exercise with instructor'),
            'packages_morning_evening_exercise': _('Morning and evening exercises with instructor'),
            'packages_yoga': _('Evening yoga and meditation'),
            'packages_hike': _('Guided sight-seeing hike'),
            'packages_horse': _('Horse riding'),
            'packages_fishing': _('Fishing'),
            'packages_activities': _('Educational and entertainment activities'),
            # Location
            'location_title': _('Location'),
            'location_paragraph_1': _('The resort Nunisi is 22 km away from the center of Kharagauli. It is 6 km from the railway station in the village of Moliti to Nunisi. The nearest settlement, the village of the same name, is located 1.5 km from the resort.'),
            'location_paragraph_2': _('Nunisi Resort is adjacent to the Borjomi-Kharagauli National Park. It is 155 km from Tbilisi, 84 km from Kutaisi, 22 km from Kharagauli and 6 km from Moliti Railway Station.'),
            'location_paragraph_3': _('A hotel minibus meets vacationers at Moliti Railway Station.'),
            # Reviews
            'review_1_content': _(
                """The city of Tskheli remained in the dust far away, 
                Nunisi - my marina, 
                Soft water and tall trees, 
                Unforgettable Nunisi days.
                """
            ),
            'review_1_name': _('Dato, 9 years old'),
            'review_2_content': _(
                """I have been receiving treatment at the Nunisi resort for two years now. I first visited the resort at the end of August last year, and the second time this year. I suffer from rheumatic disease, severe radiculitis. I was receiving treatment in our district (Lagodekhi) since March 1970, and in 1974 in Gurjaani, Akhtala, but my condition gradually became more and more difficult. For months I was chained to a bed with severe attacks and indescribable pain. Last year's treatment exceeded my expectations. If someone else had told me this, I honestly would not have believed it. I was completely cured.
                The Nunisi resort is very pleasant and convenient with its natural relief location, beauty, clean air and water. But I cannot help but express my heartfelt gratitude to the entire staff of the resort, from the director and the doctor to the cleaners. I would like to reiterate my gratitude.
                """
            ),
            'review_2_name': _('Silver Lomidze'),
            'review_3_content': _("I was at the Nunisi balneological and medical resort from August 7 to 20. There was peace and friendliness. At the same time, the resort's management was eager to improve comfort. Many thanks to the entire staff. I believe that Nunisi will become one of the best resorts in Georgia in the near future. My heart breaks as I have to leave this place tomorrow."),
            'review_3_name': _('L.Gogoladze'),
            'review_4_content': _('I was at the Nunisi Sanatorium from 25.07.02 to 8.08.02. We were amazed by the results of the healing waters, they have such a beneficial effect on skin diseases. In addition, we were amazed by the service, conditions and warm welcome of the staff.'),
            'review_4_name': _('Leila Munjishvili'),
            'review_5_content': _("I had heard about the Nunisi Baths since I was a child, but how did I know then that my little daughter would need treatment here?! When my 5-year-old daughter was diagnosed with psoriasis, I started asking people who had this incurable disease. Everyone unanimously advised me to take her  to Nunisi and get her treated. And here we are, arriving in this paradise. When I got out of the car, I couldn't hide my admiration. I liked the environment here so much. Thank you all for such warmth and attention!"),
            'review_5_name': _('Marine Laradze'),
        }

    finally:
        # If you cannot activate, activate the current language
        activate(cur_language)
    # Return translations
    return translations
