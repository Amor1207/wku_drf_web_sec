from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    # TODO: Add index page
    template = loader.get_template('guide/index.html')
    context = {
        'title': 'WKU Textbook',
    }
    return HttpResponse(template.render(context, request))

def about(request):
    # TODO: Add about page
    template = loader.get_template('guide/about.html')
    context = {
        'title': 'About',
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    # TODO: Add contact page
    template = loader.get_template('guide/contact.html')
    context = {
        'title': 'Contact',
    }
    return HttpResponse(template.render(context, request))

def faq(request):
    # TODO: Add FAQ page
    template = loader.get_template('guide/faq.html')
    context = {
        'title': 'FAQ',
    }
    return HttpResponse(template.render(context, request))

def privacy(request):
    # TODO: Add privacy page
    template = loader.get_template('guide/privacy.html')
    context = {
        'title': 'Privacy',
    }
    return HttpResponse(template.render(context, request))

def terms(request):
    # TODO: Add terms page
    template = loader.get_template('guide/terms.html')
    context = {
        'title': 'Terms',
    }
    return HttpResponse(template.render(context, request))

def help(request):
    # TODO: Add help page
    template = loader.get_template('guide/help.html')
    context = {
        'title': 'Help',
    }
    return HttpResponse(template.render(context, request))

def sitemap(request):
    template = loader.get_template('guide/sitemap.html')
    context = {
        'title': 'Sitemap',
    }
    return HttpResponse(template.render(context, request))

def robots(request):
    template = loader.get_template('guide/robots.txt')
    context = {
        'title': 'Robots',
    }
    return HttpResponse(template.render(context, request))

def ads(request):
    template = loader.get_template('guide/ads.txt')
    context = {
        'title': 'Ads',
    }
    return HttpResponse(template.render(context, request))

def favicon(request):
    template = loader.get_template('guide/favicon.ico')
    context = {
        'title': 'Favicon',
    }
    return HttpResponse(template.render(context, request))

def manifest(request):
    template = loader.get_template('guide/manifest.json')
    context = {
        'title': 'Manifest',
    }
    return HttpResponse(template.render(context, request))

def browserconfig(request):
    template = loader.get_template('guide/browserconfig.xml')
    context = {
        'title': 'Browserconfig',
    }
    return HttpResponse(template.render(context, request))

def apple_touch_icon(request):
    template = loader.get_template('guide/apple-touch-icon.png')
    context = {
        'title': 'Apple Touch Icon',
    }
    return HttpResponse(template.render(context, request))

def apple_touch_icon_120(request):
    template = loader.get_template('guide/apple-touch-icon-120x120.png')
    context = {
        'title': 'Apple Touch Icon 120',
    }
    return HttpResponse(template.render(context, request))

def apple_touch_icon_152(request):
    template = loader.get_template('guide/apple-touch-icon-152x152.png')
    context = {
        'title': 'Apple Touch Icon 152',
    }
    return HttpResponse(template.render(context, request))

def apple_touch_icon_167(request):
    template = loader.get_template('guide/apple-touch-icon-167x167.png')
    context = {
        'title': 'Apple Touch Icon 167',
    }
    return HttpResponse(template.render(context, request))

def apple_touch_icon_180(request):
    template = loader.get_template('guide/apple-touch-icon-180x180.png')
    context = {
        'title': 'Apple Touch Icon 180',
    }
    return HttpResponse(template.render(context, request))

def apple_touch_icon_60(request):
    template = loader.get_template('guide/apple-touch-icon-60x60.png')
    context = {
        'title': 'Apple Touch Icon 60',
    }
    return HttpResponse(template.render(context, request))

def apple_touch_icon_76(request):
    template = loader.get_template('guide/apple-touch-icon-76x76.png')
    context = {
        'title': 'Apple Touch Icon 76',
    }
    return HttpResponse(template.render(context, request))

def apple_touch_icon_80(request):
    template = loader.get_template('guide/apple-touch-icon-80x80.png')
    context = {
        'title': 'Apple Touch Icon 80',
    }
    return HttpResponse(template.render(context, request))

def apple_touch_icon_87(request):
    template = loader.get_template('guide/apple-touch-icon-87x87.png')
    context = {
        'title': 'Apple Touch Icon 87',
    }
    return HttpResponse(template.render(context, request))

