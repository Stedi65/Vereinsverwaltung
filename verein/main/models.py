from django.db import models
from django.db.models.base import Model, ModelState
from django.db.models.fields import CharField, IntegerField, DecimalField, EmailField, BooleanField, DateField, FilePathField


class Users(models.Model):
	nachname = models.CharField(max_length=40)
	vorname = models.CharField(max_length=40)
	alias = models.CharField(max_length=20)
	password = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	frage1 = models.CharField(null=True, blank=True, max_length=100)
	rechte = models.IntegerField(max_length=5)

    
class Funktionen(models.Model):
    funktion = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.funktion


class Beitragsgruppe(models.Model):
    gruppenname = models.CharField(max_length=40)
    beitrag = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.gruppenname


class Mitglieder(models.Model):
    nummer = models.IntegerField(max_length=6)
    anrede = models.CharField(max_length=10)
    vorname = models.CharField(max_length=40)
    nachname = models.CharField(max_length=40)
    strasse = models.CharField(max_length=40)
    plz = models.CharField(max_length=5)
    ort = models.CharField(max_length=40)
    telefon = models.CharField(null=True, blank=True, max_length=40)
    mobiltel = models.CharField(null=True, blank=True, max_length=40)
    email = models.EmailField(null=True, blank=True, max_length=100)
    werbung = models.BooleanField()
    geburtstag = models.DateField(null=True, blank=True)
    geb_anzeigen = models.BooleanField()
    austritt = models.DateField(null=True, blank=True)
    gestorben =  models.DateField(null=True, blank=True)
    beitrag = models.DecimalField(max_digits=10, decimal_places=2)
    beitragsgruppe = models.ForeignKey(Beitragsgruppe, on_delete=models.CASCADE)
    versicherungsbeitrag = models.DecimalField(max_digits=10, decimal_places=2)
    iban = models.CharField(null=True, blank=True, max_length=22)
    bic = models.CharField(null=True, blank=True, max_length=12)
    funktion = models.ForeignKey(Funktionen, on_delete=models.CASCADE)
    foto = models.FilePathField(null=True, blank=True, path='../images', match=None, recursive=False, max_length=254)
    kenntnisnachweisnr = models.CharField(null=True, blank=True, max_length=20)
    kenntnisnachweisdatum = models.DateField(null=True, blank=True)
    kenntnisnachweisgueltig = models.BooleanField()
    dmfvnummer = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self) -> str:
        return f"{self.vorname} {self.nachname}"


class Verein(models.Model):
    vereinsname = models.CharField(max_length=40)
    strasse = models.CharField(null=True, blank=True, max_length=40)
    postfach = models.CharField(null=True, blank=True, max_length=20)
    plz = models.CharField(max_length=5)
    ort = models.CharField(max_length=40)
    telefon = models.CharField(max_length=20)
    internet = models.URLField(max_length=100)
    email = models.EmailField(null=True, blank=True, max_length=100)
    datum_gruendung = models.DateField()
    vereinsregisternr = models.CharField(max_length=20)
    registergericht = models.CharField(max_length=40)
    finanzamt = models.CharField(max_length=40)
    iban1 = models.CharField(max_length=22)
    bic1 = models.CharField(max_length=12)
    bank1 = models.CharField(max_length=40)
    iban2 = models.CharField(null=True, blank=True, max_length=22)
    bic2 = models.CharField(null=True, blank=True, max_length=12)
    bank2 = models.CharField(null=True, blank=True, max_length=40)
    # models.ImageField(null=True, blank=True, upload_to="../images")
    logo_dateiname = models.FilePathField(null=True, blank=True, path='../images', match=None, recursive=False, max_length=254)

    def __str__(self) -> str:
        return self.vereinsname


class Vorstand(models.Model):
	funktion = models.ForeignKey(Funktionen, on_delete=models.CASCADE)
	datum_von = models.DateField()
	datum_bis = models.DateField(null=True, blank=True)
	mitgliednummer = models.ForeignKey(Mitglieder, on_delete=models.CASCADE)
    

class Flugmodelle(models.Model):
    mitgliednummer = models.ForeignKey(Mitglieder, on_delete=models.CASCADE)
    modellname = models.CharField(max_length=40)
    modelltyp = models.CharField(max_length=40)
    antrieb = models.CharField(max_length=40)
    spannweite = models.IntegerField(max_length=5)
    gewicht = models.IntegerField(max_length=6)
    motortyp = models.CharField(max_length=40)
    hubraum = models.IntegerField(max_length=5)
    luftschraube = models.CharField(max_length=40)
    material = models.CharField(max_length=40)
    schalldaempfer = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.modellname


class Laermpass(models.Model):
	flugmodellnr = models.ForeignKey(Flugmodelle, on_delete=models.CASCADE)
	messort = models.CharField(max_length=40)
	messdatum = models.DateTimeField()
	messbeauftragter = models.CharField(max_length=40)
	niederschlag = models.BooleanField()
	windgeschwindigkeit = models.DecimalField(max_digits=6, decimal_places=1)
	temperatur = models.DecimalField(max_digits=5, decimal_places=1)
	schallmessgeraet = models.CharField(max_length=40)
	windmessgeraet = models.CharField(max_length=40)
	thermometer = models.CharField(max_length=40)


class Beitrag(models.Model):
	datum = models.DateField()
	gueltig = models.BooleanField()
	beitrag = models.DecimalField(max_digits=8, decimal_places=2)
	versicherung1 = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)
	versicherung2 = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)
	versicherung3 = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)

    
class Beitraggruppen(models.Model):
	gruppe = models.CharField(max_length=40)
	faktor = models.DecimalField(max_digits=8, decimal_places=2)
	datum = models.DateField()

    
class Dokumente(models.Model):
	doctype = models.CharField(max_length=40)
	dokumentname = models.CharField(max_length=100)
	dateiname = models.FilePathField(path='../documents', match=None, recursive=False,max_length=254)
	mitgliednummer = models.ForeignKey(Mitglieder, on_delete=models.CASCADE)
	

class Buchungen(models.Model):
	buchungstext = models.CharField(max_length=100)
	buchungsdatum = models.DateField()
	konto = models.CharField(max_length=5)
	sollhaben = models.CharField(max_length=1)
	betrag = models.DecimalField(max_digits=10, decimal_places=2)
	gegenkonto = models.CharField(max_length=5)
	einnahmeausgabe = models.CharField(max_length=1)

