from django.urls import path
from news.views import homeview, contactview, detailsview, categoryview, getcategoryview


app_name = 'news'

urlpatterns = [
    path('', homeview, name='home'),
    path('contact/', contactview, name='contact'),
    path('details/<slug:slug>/', detailsview, name='new-detail'),
    path('categories/', categoryview, name='category'),
    path('category/<slug:slug>/', getcategoryview, name='get-category'),
]