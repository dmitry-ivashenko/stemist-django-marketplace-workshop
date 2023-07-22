from django.shortcuts import render

from item.models import Item, Category


def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html', {
        'items': items,
        'categories': categories,
    })
