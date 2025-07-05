from django.shortcuts import render
from django.conf import settings
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext


def index(request):
    '''Return the homepage'''
    context = {
        'DEBUG': settings.DEBUG,
    }
    return render(
        request,
        'homepage/index.html',
        context,
    )


def water(request):
    '''Return the water information page'''
    context = {
        'DEBUG': settings.DEBUG,
    }
    return render(
        request,
        'water/water.html',
        context,
    )


def rooms(request):
    '''Return the rooms information page'''
    standard_room_images = [
        {
            'local': 'rooms/standard_room.webp',
            'host': '',
            'alt': 'The standard room'
        },
    ]
    standard_twin_room_images = [
        {
            'local': 'rooms/standard_twin_1.webp',
            'host': 'v1749716975/standard_twin_1_l4omdb.webp',
            'alt': 'The standard twin room'
        },
        {
            'local': 'rooms/standard_twin_2.webp',
            'host': 'v1749716975/standard_twin_2_ijnahj.webp',
            'alt': 'The standard twin room'
        },
    ]
    panorama_room_images = [
        {
            'local': 'rooms/panorama_1.webp',
            'host': 'v1749716975/panorama_1_syof2m.webp',
            'alt': 'The panorma room'
        },
        {
            'local': 'rooms/panorama_2.webp',
            'host': 'v1749716975/panorama_2_aixq7s.webp',
            'alt': 'The panorma room'
        },
    ]
    suite_images = [
        {
            'local': 'rooms/suite_1.webp',
            'host': 'v1749716976/suite_1_ckyv5s.webp',
            'alt': 'The suite room'
        },
        {
            'local': 'rooms/suite_2.webp',
            'host': 'v1749716976/suite_2_voka4c.webp',
            'alt': 'The suite room'
        },
    ]
    family_room_images = [
        {
            'local': 'rooms/family_room_1.webp',
            'host': 'v1749716975/family_room_1_lksgpo.webp',
            'alt': 'The family room'
        },
        {
            'local': 'rooms/family_room_2.webp',
            'host': 'v1749716975/family_room_2_yiir0p.webp',
            'alt': 'The family room'
        },
    ]
    context = {
        'DEBUG': settings.DEBUG,
        # Images
        'standard_room_images': standard_room_images,
        'standard_twin_room_images': standard_twin_room_images,
        'panorama_room_images': panorama_room_images,
        'suite_images': suite_images,
        'family_room_images': family_room_images,
    }
    return render(
        request,
        'rooms/rooms.html',
        context,
    )


def gallery(request):
    '''Return the gallery page'''
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
    }
    return render(
        request,
        'gallery/gallery.html',
        context,
    )
