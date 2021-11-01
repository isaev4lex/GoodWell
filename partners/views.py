from django.shortcuts import render
from contacts.models import *
from site_settings.models import *
from .models import *


def partners(request, lang='ru'):
    data = {
        'page': 'partners',
        'partners': Partners.objects.all(),
        'meta': MetaTags.objects.all(),
        'favicons': Favicon.objects.all(),
        'head_tags': HeadTags.objects.all(),
        'lang': lang,
        'contact_info': {
            'phones': Phone.objects.all(),
            'emails': EMail.objects.all(),
            'addresses': Address.objects.all(),
            'social': SocialLink.objects.all()
        },
    }
    return render(request, 'partners/index.html', context=data)
