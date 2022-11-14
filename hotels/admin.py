from django.contrib import admin
from .models import HotelAdmin, Hotel, Place

admin.site.register(Hotel)
admin.site.register(HotelAdmin)
admin.site.register(Place)
