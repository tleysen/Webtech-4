from django.shortcuts import render
from .models import Quote
from .models import Author


def index(request):
    latest_quote_list = Quote.objects.order_by('-pub_date')[:5]
    context = {
        'latest_quote_list': latest_quote_list,
    }
    return render(request, 'Recipes/index.html', context)

def detail(request, quote_id):
    quote =  Quote.objects.filter(id = quote_id)
    author = Author.objects.filter(Quote_id = quote_id)

    context = {
        'author' : author,
        'quote' : quote,
    }
    return render(request, 'Recipes/detail.html', context)
