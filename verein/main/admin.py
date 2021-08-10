from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Users)
admin.site.register(Mitglieder)
admin.site.register(Verein)
admin.site.register(Funktionen)
admin.site.register(Vorstand)
admin.site.register(Beitrag)
admin.site.register(Beitraggruppen)
admin.site.register(Buchungen)
admin.site.register(Dokumente)