from django.urls import path 
from . import views

urlpatterns = [
    path("/", views.home, name="home"),
    path("", views.home, name="home" ),
    path("messbericht/<str:modeltyp>", views.messbericht, name="messbericht"),
    path("mitgliederliste/", views.show_mitglieder, name="mitglieder"),
    path("mitglied_add/", views.add_mitglied, name="mitglied_add"),
    path("vereinsdaten/", views.vereinsdaten, name='vereinsdaten'),
    path("vorstand/", views.vorstand, name='vorstand')
]