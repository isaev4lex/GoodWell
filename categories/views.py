from django.shortcuts import render
from contacts.models import *
from site_settings.models import *
from .models import *
import os


def categories(request, lang='ru', slug=None):
    data = {
        'slug': slug,
        'page': 'categories',
        'categories': [],
        'products': [],
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

    if slug == 'paints':
        data['products'].append(Paint.objects.all())
        for i in Category.objects.all():
            if i.title == 'Огнезащитные краски':
                data['categories'].append(i)
        return render(request, 'categories/index.html', context=data)
    elif slug == 'mixes':
        data['products'].append(FlameRetard.objects.all())
        for i in Category.objects.all():
            if i.title == 'Огнезащитные составы':
                data['categories'].append(i)
        return render(request, 'categories/index.html', context=data)
    elif slug == 'tubes' or slug == 'fitting':
        data['products'].append(Tubes.objects.all())
        data['products'].append(Fitting.objects.all())
        for i in Category.objects.all():
            if i.title == 'Огнеупорные трубы' or i.title == 'Огнеупорные фитинги':
                data['categories'].append(i)
        return render(request, 'categories/index.html', context=data)
    elif slug == 'alarms':
        data['products'].append(Alarm.objects.all())
        for i in Category.objects.all():
            if i.title == 'Противопожарное оборудование':
                data['categories'].append(i)
        return render(request, 'categories/index.html', context=data)
