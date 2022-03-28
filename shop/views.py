from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from .models import *


# Create your views here.

def home(request, c_slug=None):
    c_page = None
    prodt = None
    if c_slug is not None:
        c_page = get_object_or_404(categ, slug=c_slug)
        prodt = product.objects.filter(category=c_page, available=True)
    else:
        prodt = product.objects.all().filter(available=True)
    cat = categ.objects.all()
    paginator = Paginator(prodt, 12)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'pr': prodt, 'ct': cat, 'pg': pro})


def prodDetails(request, c_slug, product_slug):
    try:
        prod = product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'details.html', {'pr': prod})


def searching(request):
    prod = None
    qurey = None
    if 'q' in request.GET:
        qurey = request.GET.get('q')
        prod = product.objects.all().filter(Q(name__contains=qurey) | Q(desc__contains=qurey))
    return render(request, 'search.html', {'qr': qurey, 'pr': prod})
