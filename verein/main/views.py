from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.models import *
from .forms import (
    LearmpassModelForm,
    MitgliedModelForm,
    VereinModelForm,
    VorstandModelForm,
)
import pdfkit


def home(response):
    #return HttpResponse("<h1> This is Home </h1>")
    return render(response, "main/home.html", {})


def messbericht(response, modeltyp):
    html_page = "main/Messbericht-" + modeltyp + ".html"
    form = LearmpassModelForm
    if modeltyp == "Motormodel" and response.method == "GET":
        return render(response, html_page, {})

    if modeltyp == "Motormodel" and response.method == "POST":
        form = LearmpassModelForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        context = {"form": form}
        return render(response, html_page, context)

    if modeltyp == "Hubi":
        pass

    if modeltyp == "Turbine":
        pass


def show_mitglieder(response):
    mitglieder = Mitglieder.objects.all()      
    return render(response, "main/mitglieder.html", {"mitglieder": mitglieder})


def add_mitglied(request):
    form = MitgliedModelForm
    if request.method == "POST":
        form = MitgliedModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "main/mitglied_add.html", context)


def vereinsdaten(request):
    form = VereinModelForm
    if request.method == "POST":
        form = VereinModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "main/vereinsdaten.html", context)


def vorstand(request):
    form = VorstandModelForm
    if request.method == "POST":
        form = VorstandModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "main/vorstand.html", context)


def make_pdf(html_file, out_file):
    pdfkit.from_url(html_file, out_file)
    
