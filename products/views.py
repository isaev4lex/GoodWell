from django.shortcuts import render
from contacts.models import *
from categories.models import *
from site_settings.models import *
from partners.models import Partners
from .models import *
import os


def product(request, lang='ru', slug=None):
    data = {
        'slug': slug,
        'page': 'product',
        'notech': False,
        'categories': [],
        'products': [Paint.objects.all(), FlameRetard.objects.all(), Tubes.objects.all()],
        'technic_info': TechnicInfo.objects.all(),
        'technic_tubes_info': TechnicTubesInfo.objects.all(),
        'meta': MetaTags.objects.all(),
        'favicons': Favicon.objects.all(),
        'head_tags': HeadTags.objects.all(),
        'lang': lang,
        'contact_info': {
            'phones': Phone.objects.all(),
            'emails': EMail.objects.all(),
            'addresseproducts': Address.objects.all(),
            'social': SocialLink.objects.all()
        },
    }
    contact_info = {
        'name': request.GET.get('name'),
        'phone': request.GET.get('phone'),
        'company': request.GET.get('company'),
        'message': request.GET.get('message'),
    }
    if not contact_info['name'] or not contact_info['phone'] or not contact_info['message']:
        pass
    else:
        os.system(
            f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" '
            f'--company "{contact_info["company"]}" --message "{contact_info["message"]}"')
        data['success_sent'] = True

    return render(request, 'products/index.html', context=data)
