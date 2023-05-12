from django.contrib import admin

from juegosApp.models import Stock, FreeStock, FreeGames, PayGames

admin.site.register(Stock)

admin.site.register(FreeStock)

admin.site.register(FreeGames)

admin.site.register(PayGames)

# Register your models here.
