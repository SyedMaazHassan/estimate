from application.forms import base_valuesForm
from django.contrib import admin
from django.db.models import base
from .models import *
# from .forms import *


class base_valuesAdmin(admin.ModelAdmin):
    # list_display= ('title', 'author', 'description', 'publicationyear')
    list_display = [
            "site_number",
            "truck_per_mile",
            "trailer_per_day",
            "fuel_rate",
            "avg_work_truck_mpg",
            "avg_tower_tech",
            "avg_civil_tech",
            "loaging_rate",
            "m_i_rate",
            "warehouse_log_rate",
            "sg_a_overhead_rate",
            "desired_margin"
        ]
    
    list_editable = list_display[1:]
    search_fields = ["site_number"]
    

# Register your models here.
admin.site.register(base_values, base_valuesAdmin)