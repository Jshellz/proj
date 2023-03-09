from django.contrib import admin

from .models import House, Flat, NewConstruction, Land

# Register your models here.


admin.site.register(House)
admin.site.register(Land)
admin.site.register(NewConstruction)
admin.site.register(Flat)
