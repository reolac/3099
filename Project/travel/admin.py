from django.contrib import admin

from .models import Venue

from .models import CinemaLocs




class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_Name', 'venue_Location', 'venue_Category')


admin.site.register(Venue, VenueAdmin)