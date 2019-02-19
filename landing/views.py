from django.shortcuts import render
from .forms import BuyersForm
from products.models import *
# Create your views here.
def landing(request):

    form = BuyersForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_underwears = products_images.filter(product__type__id=3)
    products_images_homewears = products_images.filter(product__type__id=2)
    products_images_waterwears = products_images.filter(product__type__id=1)
    products_images_manwears = products_images.filter(product__type__id=4)
    products_images_newarrives = products_images.filter(product__type__id=5)
    return render(request, 'landing/home.html', locals())
