from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import fields
from .models import Dokumente, Funktionen, Laermpass, Mitglieder, Users, Verein, Vorstand, Beitrag, Beitraggruppen, Beitragsgruppe, Buchungen


class MitgliedModelForm(forms.ModelForm):
    class Meta:
        model = Mitglieder
        fields = '__all__'


class VereinModelForm(forms.ModelForm):
    class Meta:
        model = Verein
        fields = '__all__'


class UsersModelForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class VorstandModelForm(forms.ModelForm):
    class Meta:
        model = Vorstand
        fields = '__all__'


class FunktionenModelForm(forms.ModelForm):
    class Meta:
        model = Funktionen
        fields = '__all__'


class BeitragModelForm(forms.ModelForm):
    class Meta:
        model = Beitrag
        fields = '__all__'


class BeitraggruppenModelForm(forms.ModelForm):
    class Meta:
        model = Beitraggruppen
        fields = '__all__'


class BeitragsgruppeModelForm(forms.ModelForm):
    class Meta:
        model = Beitragsgruppe
        fields = '__all__'


class BuchungenModelForm(forms.ModelForm):
    class Meta:
        model = Buchungen
        fields = '__all__'


class DokumenteModelForm(forms.ModelForm):
    class Meta:
        model = Dokumente
        fields = '__all__'

class LearmpassModelForm(forms.ModelForm):
    class Meta:
        model = Laermpass
        fields = '__all__'

        