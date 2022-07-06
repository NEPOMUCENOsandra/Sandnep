from django.contrib import admin
from django.urls import path
from . import views

app_name = 'soapsystem'

urlpatterns = [
    path('',views.Mainpage, name='Mainpage'),
    path('Aboutshop/',views.Aboutshop, name='Aboutshop'),
    path('Soaps/',views.Soaps, name='Soaps'),
    path('SoapBuy/',views.SoapBuy, name='SoapBuy'),
    path('buyerinfor',views.buyerinfor, name='buyerinfor'),
    path('Topay/',views.Topay, name='Topay'),
    path('ContactForm/',views.ContactForm, name='ContactForm'), 
    path('Feedback/',views.Feedback, name='Feedback'),
    ]