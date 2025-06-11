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
        # Site Header
        'site_header_home': trans['site_header_home'],
        'site_header_water': trans['site_header_water'],
        'site_header_rooms': trans['site_header_rooms'],
        'site_header_photo': trans['site_header_photo'],
        'call_us': trans['call_us'],
        # Site Footer
        'contact_us': trans['contact_us'],
        'copywrite': trans['copywrite'],
        'developer': trans['developer'],
        'follow_us': trans['follow_us'],
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


def water(request):
    '''Return the water information page'''
    trans = translate(language=get_language() or settings.LANGUAGE_CODE)
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'DEBUG': settings.DEBUG,
        # Translations
        # Site Header
        'site_header_home': trans['site_header_home'],
        'site_header_water': trans['site_header_water'],
        'site_header_rooms': trans['site_header_rooms'],
        'site_header_photo': trans['site_header_photo'],
        'call_us': trans['call_us'],
        # Site Footer
        'contact_us': trans['contact_us'],
        'copywrite': trans['copywrite'],
        'developer': trans['developer'],
        'follow_us': trans['follow_us'],
        # Water copied from homepage
        'water_title': trans['water_title'],
        'water_paragraph_1': trans['water_paragraph_1'],
        'water_paragraph_2': trans['water_paragraph_2'],
        # Extra paragraphs
        'water_paragraph_3': trans['water_paragraph_3'],
        'water_paragraph_4': trans['water_paragraph_4'],
        'water_composition_title': trans['water_composition_title'],
        'water_composition_paragraph_1': trans['water_composition_paragraph_1'],
        'water_composition_paragraph_2': trans['water_composition_paragraph_2'],
        'water_composition_paragraph_3': trans['water_composition_paragraph_3'],
        'water_composition_paragraph_4': trans['water_composition_paragraph_4'],
        'water_composition_paragraph_5': trans['water_composition_paragraph_5'],
    }
    return render(
        request,
        'water/water.html',
        context,
    )


def rooms(request):
    '''Return the rooms information page'''
    trans = translate(language=get_language() or settings.LANGUAGE_CODE)
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'DEBUG': settings.DEBUG,
        # Translations
        # Site Header
        'site_header_home': trans['site_header_home'],
        'site_header_water': trans['site_header_water'],
        'site_header_rooms': trans['site_header_rooms'],
        'site_header_photo': trans['site_header_photo'],
        'call_us': trans['call_us'],
        # Site Footer
        'contact_us': trans['contact_us'],
        'copywrite': trans['copywrite'],
        'developer': trans['developer'],
        'follow_us': trans['follow_us'],
        # Page Header
        'packages': trans['packages'],
        'rooms': trans['rooms'],
        'cottages': trans['cottages'],
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
        'packages_2_people': trans['packages_2_people'],
        'packages_4_people': trans['packages_4_people'],
        # Rooms
        'rooms_title': trans['rooms_title'],
        'standard_room_title': trans['standard_room_title'],
        'standard_double_room_title': trans['standard_double_room_title'],
        'panarama_room_title': trans['panarama_room_title'],
        'suite_room_title': trans['suite_room_title'],
        'family_room_title': trans['family_room_title'],
        'room_occupancy_2': trans['room_occupancy_2'],
        'room_occupancy_4': trans['room_occupancy_4'],
        'room_occupancy_5': trans['room_occupancy_5'],
        'standard_room_description': trans['standard_room_description'],
        'standard_double_room_description': trans['standard_double_room_description'],
        'suite_room_description': trans['suite_room_description'],
        'family_room_description': trans['family_room_description'],
        'bathroom_description': trans['bathroom_description'],
        'bathroom_description_suite': trans['bathroom_description_suite'],
        'amenity_bathroom': trans['amenity_bathroom'],
        'amenity_fridge': trans['amenity_fridge'],
        'amenity_wifi': trans['amenity_wifi'],
        'amenity_tv': trans['amenity_tv'],
        'amenity_cable': trans['amenity_cable'],
        # Cottages
        'cottages_paragraph_1': trans['cottages_paragraph_1'],
        'cottages_paragraph_2': trans['cottages_paragraph_2'],
    }
    return render(
        request,
        'rooms/rooms.html',
        context,
    )


def gallery(request):
    '''Return the gallery page'''
    trans = translate(language=get_language() or settings.LANGUAGE_CODE)
    image_filenames = [
        {
            'local': 'gallery/1_main_house_day.webp',
            'host': 'v1747244369/main_house_day_ui6vtj.webp',
            'alt': 'Main house during the day.'
        },
        {
            'local': 'gallery/2_main_path.webp',
            'host': 'v1747244366/main_path_coisvd.webp',
            'alt': 'The main path in the resort',
        },
        {
            'local': 'gallery/3_church.webp',
            'host': 'v1747244367/church_ey2gr7.webp',
            'alt': 'The chapel at the resort',
        },
        {
            'local': 'gallery/4_main_house_night.webp',
            'host': 'v1747244369/main_house_night_fcsmin.webp',
            'alt': 'The main house at night',
        },
        {
            'local': 'gallery/bench_2.webp',
            'host': 'v1749619964/bench_2_acs7fv.webp',
            'alt': 'A bench at the resort',
        },
        {
            'local': 'gallery/bench.webp',
            'host': 'v1749619991/bench_dv6t39.webp',
            'alt': 'A bench near the chapel',
        },
        {
            'local': 'gallery/cable_car_1.webp',
            'host': 'v1749620062/cable_car_1_akgzxh.webp',
            'alt': 'The cable car half way across the gorge',
        },
        {
            'local': 'gallery/cable_car_2.webp',
            'host': 'v1749620861/cable_car_2_uiz46o.webp',
            'alt': 'The cable car',
        },
        {
            'local': 'gallery/cable_car_3.webp',
            'host': 'v1749620933/cable_car_3_nwha3g.webp',
            'alt': 'The cable car half way across the gorge',
        },
        {
            'local': 'gallery/cable_car_4.webp',
            'host': 'v1749620924/cable_car_4_malpaj.webp',
            'alt': 'The cable car',
        },
        {
            'local': 'gallery/cable_car_5.webp',
            'host': 'v1749620926/cable_car_5_suvfyx.webp',
            'alt': 'The cable car',
        },
        {
            'local': 'gallery/cable_car_6.webp',
            'host': 'v1749620928/cable_car_6_soyjse.webp',
            'alt': 'The cable car',
        },
        {
            'local': 'gallery/cottage_1.webp',
            'host': 'v1749563409/cottage_1_jyf14u.webp',
            'alt': 'One of the cottages from outside',
        },
        {
            'local': 'gallery/cottage_2.webp',
            'host': 'v1749563409/cottage_2_xwnjzo.webp',
            'alt': 'The top floor of a cottage',
        },
        {
            'local': 'gallery/cottage_3.webp',
            'host': 'v1749563409/cottage_3_sm6l4c.webp',
            'alt': 'The top floor of a cottage',
        },
        {
            'local': 'gallery/cottage_4.webp',
            'host': 'v1749563409/cottage_4_mmwnxv.webp',
            'alt': 'The ground floor of a cottage',
        },
        {
            'local': 'gallery/cottage_5.webp',
            'host': 'v1749563409/cottage_5_hpfm4y.webp',
            'alt': 'A flower outside one of the cottages',
        },
        {
            'local': 'gallery/cottage_6.webp',
            'host': 'v1749563409/cottage_6_x4masn.webp',
            'alt': 'One of the cottages from outside',
        },
        {
            'local': 'gallery/cottage_outside.webp',
            'host': 'v1749563409/cottage_outside_bdlfbi.webp',
            'alt': 'One of the cottages from outside',
        },
        {
            'local': 'gallery/dog.webp',
            'host': 'v1749620247/dog_wfemjh.webp',
            'alt': 'A dog on the path in Nunisi',
        },
        {
            'local': 'gallery/forest_trees_2.webp',
            'host': 'v1748526899/forest_trees_2_qjrxnj.webp',
            'alt': 'A view up through the tree canopy',
        },
        {
            'local': 'gallery/forest_trees_night.webp',
            'host': 'v1749620322/forest_trees_night_nhc2af.webp',
            'alt': 'A view up through the tree canopy at night',
        },
        {
            'local': 'gallery/forest_trees.webp',
            'host': 'v1749620351/forest_trees_csr4lu.webp',
            'alt': 'A view up through the tree canopy',
        },
        {
            'local': 'gallery/main_house_main_room.webp',
            'host': 'v1749620403/main_house_main_room_k7hw57.webp',
            'alt': 'The main guest room at the main house',
        },
        {
            'local': 'gallery/main_house_other_room.webp',
            'host': 'v1749620440/main_house_other_room_aembqv.webp',
            'alt': 'A side guest room at the main house',
        },
        {
            'local': 'gallery/main_house_side_room_2.webp',
            'host': 'v1749620467/main_house_side_room_2_i1p7ho.webp',
            'alt': 'A side guest room at the main house',
        },
        {
            'local': 'gallery/nunisi_view.webp',
            'host': 'v1749620513/nunisi_view_xkjz2f.webp',
            'alt': 'A view over the Nunisi mountains',
        },
        {
            'local': 'gallery/path_2.webp',
            'host': 'v1749620579/path_2_r3cfnr.webp',
            'alt': 'One of the paths at the site',
        },
        {
            'local': 'gallery/path_3.webp',
            'host': 'v1749620571/path_3_xmswas.webp',
            'alt': 'One of the paths at the site',
        },
        {
            'local': 'gallery/path_4.webp',
            'host': 'v1749620577/path_4_fw8o4v.webp',
            'alt': 'One of the paths at the site',
        },
        {
            'local': 'gallery/path_5.webp',
            'host': 'v1749620572/path_5_sur0kx.webp',
            'alt': 'One of the paths at the site',
        },
        {
            'local': 'gallery/path_6.webp',
            'host': 'v1749620576/path_6_gqwvge.webp',
            'alt': 'One of the paths at the site',
        },
        {
            'local': 'gallery/path_night.webp',
            'host': 'v1749620930/path_night_im3njp.webp',
            'alt': 'One of the paths at night',
        },
        {
            'local': 'gallery/path.webp',
            'host': 'v1749620574/path_a390ub.webp',
            'alt': 'One of the paths at the site',
        },
        {
            'local': 'gallery/standard_room.webp',
            'host': 'v1749546955/standard_room_wl0ojg.webp',
            'alt': 'A side guest room at the main house',
        },
        {
            'local': 'gallery/view.webp',
            'host': 'v1748525445/view_eavxrt.webp',
            'alt': 'A view through the trees of the mountains',
        },
        {
            'local': 'gallery/water_2.webp',
            'host': 'v1748524815/water_2_csbrun.webp',
            'alt': 'A waterfall in Nunisi',
        },
        {
            'local': 'gallery/woodland_path.webp',
            'host': 'v1747244367/woodland_path_myzxuz.webp',
            'alt': 'A forest path',
        },
    ]
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'DEBUG': settings.DEBUG,
        # Images
        'images': image_filenames,
        # Translations
        # Site Header
        'site_header_home': trans['site_header_home'],
        'site_header_water': trans['site_header_water'],
        'site_header_rooms': trans['site_header_rooms'],
        'site_header_photo': trans['site_header_photo'],
        'call_us': trans['call_us'],
        # Site Footer
        'contact_us': trans['contact_us'],
        'copywrite': trans['copywrite'],
        'developer': trans['developer'],
        'follow_us': trans['follow_us'],
    }
    return render(
        request,
        'gallery/gallery.html',
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
            # Site Header
            'site_header_home': _('Home'),
            'site_header_water': _('Nunisi Water'),
            'site_header_rooms': _('Build Your Stay'),
            'site_header_photo': _('Photo Gallery'),
            'call_us': _('Call us today on'),
            # Site Footer
            'contact_us': _('Contact us'),
            'copywrite': _('Nunisi Hotel and Spa. All rights reserved'),
            'developer': _('Developed by'),
            'follow_us': _('Follow us on social media'),
            # Index: Header
            'header_link_about_us': _('About Us'),
            'header_link_nunisi_water': _('Nunisi Water'),
            'header_link_services': _('Services'),
            'header_link_location': _('Location'),
            'header_link_reviews': _('Reviews'),
            # Index: Hero Image
            'hotel_name': _('Nunisi Forest Hotel and Spa'),
            'welcome_message': _('Where luxury is natural!'),
            # Index: Booking
            'booking_title': _('Book now via'),
            'booking_email': _(' Email: '),
            'booking_phone': _(' Phone: (+995) 599 22 55 80'),
            'booking_through': _('Through '),
            'booking_or': _('or'),
            'booking_booking_com': _('Book through booking.com'),
            'booking_rooms_button': _('Take a look at our rooms & packages'),
            # Index: About Us
            'about_us_carousel_prev': _('About Us'),
            'about_us_carousel_next': _('The Legend of Nunisi'),
            'about_us_title': _('A unique resort of world importance'),
            'about_us_paragraph': _("Nunisi mineral water was known as early as the 17th century. The balneological resort has been hosting those who want to relax in picturesque nature since 1856. It cures skin diseases and rehabilitates health in conditions of deep relaxation. Naturally warm, gas-filled water baths containing flint, sulfur, and other minerals achieve amazing healing results. Mixed forest, old trees, green surroundings, healing air, baths, and natural products are the best for deep relaxation and restoration of strength."),
            'about_us_legend': _('The Legend of Nunisi'),
            'about_us_legend_text_1': _('There is a legend about the discovery of Nunisi water, which is associated with the great Georgian king, David the Builder. The legend tells us that King David was returning from a battle. His horses, tired from walking, whose skin was peeling and sores were forming, they lay down in the Nunisi water and soon recovered. The overjoyed king made a large donation to the temple in the village. The Nunisi Monastery of the Nativity of the Virgin Mary, built in the 9th-10th centuries, is still in operation today.'),
            'about_us_legend_text_2': _('The healing use of Nunisi water has been known since the 9th century. The population noticed that their pets were being cured of malaise with the help of the mineral water, tried using it themselves and got results. Over time, the whole of Georgia learned about the healing properties of the springs. The water of Nunisi was called “a garment and a blessing” by the 18th-century Georgian geographer Vakhushti Batonishvili and is actively mentioned in his works.'),
            # Index: Water
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
            # Index: Services
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
            # Index: Location
            'location_title': _('Location'),
            'location_paragraph_1': _('The resort Nunisi is 22 km away from the center of Kharagauli. It is 6 km from the railway station in the village of Moliti to Nunisi. The nearest settlement, the village of the same name, is located 1.5 km from the resort.'),
            'location_paragraph_2': _('Nunisi Resort is adjacent to the Borjomi-Kharagauli National Park. It is 155 km from Tbilisi, 84 km from Kutaisi, 22 km from Kharagauli and 6 km from Moliti Railway Station.'),
            'location_paragraph_3': _('A hotel minibus meets vacationers at Moliti Railway Station.'),
            # Index: Reviews
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
            # Water page: Water paragraphs
            'water_paragraph_3': _(
                """Treatment and remission with medication is often a problem. A dermatologist diagnoses and prescribes treatment with natural remedies. The course of treatment is often long and complex. In some cases, chronic skin diseases are accompanied by such annoying symptoms as: itching, dry skin, burning, pain, discomfort...Which, of course, is associated with skin rashes and therefore is often the basis for the patient's psychological problems: self-esteem and quality of life decrease, stress, anxiety, depression, feelings of hopelessness increase. This is where the Nunisi Baths come as a savior and helper, thanks to which many hopeless patients have regained hope and joy of life, forgetting about skin problems and accompanying annoying symptoms. Of these skin diseases, psoriasis is a fairly common nosology. It is a chronic disease characterized by psoriatic papules and plaques covered with scales and crusts. It is mainly localized on the limbs, the hairy area of the head, and not infrequently on the body. It is often accompanied by itching, and damage to small and large joints may be observed - psoriatic arthritis, damage to nails (hourglass nails). Genetic predisposition and family history are very important in psoriasis. Psoriasis is a progressive disease with flare-ups and remissions (periods without a rash). The cause of exacerbation can be stress, emotional factors, skin trauma (Koebner phenomenon), surgery, wounds, burns, taking certain medications, infectious diseases, various underlying diseases, etc.
                    For such patients, it is very important to bring the disease into remission and prolong it, and balneotherapy procedures with Nunisi water will make an irreplaceable contribution and help you in all this. Nunis water also has an extraordinary effect in the case of atopic dermatitis. The latter is one of the most common chronic allergic diseases in childhood. However, it can also be found in other age groups, developing in individuals genetically predisposed to atopy. During this time, the skin's sensitivity to specific and nonspecific irritants increases. It is characterized primarily by dry skin, peeling, exudative or lichenoid rashes, and cracks. It is often accompanied by bothersome itching, burning, pain, discomfort, disturbed sleep, increased emotional background, and a high risk of developing secondary infections.
                """
            ),
            'water_paragraph_4': _("The solution is the unique Nunisi baths, which have no analogues in the world."),
            'water_composition_title': _('Composition of our mineral water'),
            'water_composition_paragraph_1': _("Nunisi water is distinguished by its low mineralization and high alkalinity (- PH 8.3 – 10.4). It is a weakly sulfide, chloride, hydrocarbonate, sodium, subthermal water with an average temperature of 27 degrees. It is rich in silicic acid, biologically active substances and antioxidants, as well as such microelements and ions as: potassium, calcium, iron, bromine, chlorine, iodine, etc."),
            'water_composition_paragraph_2': _(
                """Water contains dissolved gas in the range of 20-28 mg. Nitrogen predominates by mass and smaller amounts of methane and hydrogen sulfide. Its composition ensures good penetration into the skin and the ability to affect the deeper layers of the skin, which in turn has a positive therapeutic effect in chronic dermatoses. It has anti-inflammatory, exfoliating, and soothing effects. More specifically, thanks to its high alkalinity, it removes and removes the upper rough layers of the skin, penetrates deep into the lower layers, and delivers all the necessary healing minerals and substances that are contained in it. It happens so quickly, the skin absorbs water so well, that after getting out of the water, patients note that the traces of water on the skin disappear within a few seconds, as if they were dried with a towel. This is also called the injection effect.
                    As a result of balneotherapy procedures performed with Nunis water, the patient achieves a long-term remission of chronic dermatoses, which may last from several months to several years, or a complete cure.
                """
            ),
            'water_composition_paragraph_3': _("The annoying itching and discomfort are eliminated, the rash is reduced or completely disappears, sleepless nights and low self-esteem are forgotten. But, of course, this result cannot be achieved in one day. It is necessary to follow the doctor's recommendations precisely and consistently, conduct one or more courses of procedures, and gradually increase or adjust the duration of the procedures. It should be noted that Nunisi water has a positive effect not only on the skin, but also on a number of diseases of the peripheral nervous system and musculoskeletal system."),
            'water_composition_paragraph_4': _("Before starting the Nunis balneotherapy course, you will undergo a consultation with a dermatologist or, if necessary, a therapist. You will receive comprehensive information about your illness and a balneotherapy course will be planned."),
            'water_composition_paragraph_5': _("For many grateful patients, results have already been achieved with the help of the excellent baths and environment of the Nunisi Resort."),
            # Rooms page: Header
            'packages': _('Packages'),
            'rooms': _('Rooms'),
            'cottages': _('Cottages'),
            # Rooms page: Packages
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
            'packages_2_people': _('This package is for 2 people'),
            'packages_4_people': _('This package is for 4 people'),
            # Rooms page: Rooms
            'rooms_title': _("Where you'll stay"),
            'standard_room_title': _('Standard Room'),
            'standard_double_room_title': _('Standard Double Room'),
            'panarama_room_title': _('Panarama Room'),
            'suite_room_title': _('Suite'),
            'family_room_title': _('Family Room'),
            'room_occupancy_2': _('This room is suitable for a maximum of 2 people.'),
            'room_occupancy_4': _('This room is suitable for a maximum of 4 people.'),
            'room_occupancy_5': _('This room is suitable for a maximum of 5 people.'),
            'standard_room_description': _('A room with twin beds, desk, chair, complimentary tea/coffee maker, mini refrigerator, plasma TV, Wi-Fi. '),
            'standard_double_room_description': _('Modern design room with double bed, chairs, coffee table, mini refrigerator, Complimentary tea / coffee maker, TV, WiFi.'),
            'suite_room_description': _('A modern room with queen bed, sofa, three chairs, coffee table mini refrigerator, complimentary tea/coffee maker, plasma TV set, Wi-Fi.'),
            'family_room_description': _('A modern room with several beds, sofa, chairs, coffee table, complimentary tea/coffee, mini refrigerator, plasma TV, Wi-Fi.'),
            'bathroom_description': _('Bathroom equipped with all necessary hygiene amenities.'),
            'bathroom_description_suite': _('Bathroom equipped with all necessary hygiene amenities, bathrobes and a hairdryer.'),
            'amenity_bathroom': _('Private bathroom'),
            'amenity_fridge': _('Mini refrigerator'),
            'amenity_wifi': _('Free WiFi'),
            'amenity_tv': _('TV'),
            'amenity_cable': _('Satellite and Cable Channels'),
            # Rooms page: cottages
            'cottages_paragraph_1': _('There are five standard cottages at the resort. They are wooden Finnish-style cottages. Each of them is two-story and consists of three rooms. The rooms are equipped with their own bathrooms (washbasin, shower and toilet).'),
            'cottages_paragraph_2': _('On the first floor there is a lobby with a TV and one triple room. On the second floor there are two rooms with their own bathrooms, one with a double bed and one with a single bed.'),
        }

    finally:
        # If you cannot activate, activate the current language
        activate(cur_language)
    # Return translations
    return translations
