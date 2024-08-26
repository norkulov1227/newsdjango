from django.shortcuts import render
from news.models import News, Category
from news.forms import ContactForm
from django.contrib import redirects

# Create your views here.

def homeview(request):
    news = News.objects.all()
    categories = Category.objects.all()
    latest_news = news.order_by('-created_at')[:6]
    category = categories.order_by('created_at')[:4]
    rand_news = news.order_by('?')[:9]
    most_read = news.order_by('-view')[:5]
    context = {
        'latest_news' : latest_news,
        'categories' : category,
        'rand_news' : rand_news,
        'most_read' : most_read
    }
    return render(request, 'index.html', context)

def contactview(request):
    form = ContactForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()        
    return render(request, 'contact.html', {'form' : form})

def detailsview(request, slug):
    news = News.objects.all()
    new = News.objects.get(slug = slug)
    category = Category.objects.all()
    most_read = news.order_by('-view')[:5]
    latest_new = news.order_by('-created_at')[:5]

    context = {
        'new' : new,
        'categories' : category,
        'most_read' : most_read,
        'latest_news' : latest_new
    }
    return render(request, 'single-page.html', context)

def categoryview(request):
    category = Category.objects.all()
    context = {
        'categories' : category
    }
    return render(request, 'category.html', context)

def getcategoryview(request, slug):
    category = Category.objects.get(slug = slug)
    new = News.objects.all().order_by('?')

    context = {
        'news' : new,
        'category' : category
    }
    return render(request, 'get_category.html', context)