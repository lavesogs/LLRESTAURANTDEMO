from django.contrib import admin
from .models import Menu
from .models import Booking

# Register your models here.
admin.site.register(Menu)

class BookingAdmin(admin.ModelAdmin): 
    list_display = ('customer_name', 'booking_date', 'booking_time', 'table_number') 
    search_fields = ('customer_name', 'booking_date')