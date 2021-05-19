from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth
# Create your models here.

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver

class estimate_inputs(models.Model):
    current_date                = models.DateField(default = datetime.now().date())
    construnction_start_date    = models.DateField()
    target_price                = models.FloatField(blank = True)
    carrier                     = models.CharField(max_length = 255)
    landlord                    = models.CharField(max_length = 255)
    turf_vendor                 = models.CharField(max_length = 255)
    site_name                   = models.CharField(max_length = 255)
    latitude                    = models.FloatField()
    longitude                   = models.FloatField()
    is_tower_work               = models.CharField(max_length = 255, choices=[("yes", "YES"), ("no", "No")])
    towers_personnel            = models.IntegerField()
    expected_tower_working_days = models.IntegerField()
    expected_tower_working_hours= models.IntegerField()
    tower_trucks                = models.IntegerField()
    tower_trailers              = models.IntegerField()
    is_civil_work               = models.CharField(max_length = 255, choices=[("yes", "YES"), ("no", "No")])
    civil_personnel             = models.IntegerField()
    expected_civil_working_days = models.IntegerField()
    expected_civil_working_hours= models.IntegerField()
    civil_trucks                = models.IntegerField()
    civil_trailers              = models.IntegerField()
    is_box_trucks_used          = models.CharField(max_length = 255, choices=[("yes", "YES"), ("no", "No")])
    box_trcuk_utilization       = models.CharField(max_length = 255)
    is_perdiem                  = models.CharField(max_length = 255, choices=[("yes", "YES"), ("no", "No")])
    expected_perdiem_working_days = models.IntegerField()
    days_on_perdiem             = models.IntegerField()
    distance_to_site            = models.IntegerField()


class base_values(models.Model):
    site_number	        = models.CharField(max_length = 255, verbose_name="Site number")
    truck_per_mile      = models.FloatField( verbose_name="Truck Per Mile")
    trailer_per_day     = models.FloatField( verbose_name="Trailer Per Day")
    fuel_rate           = models.FloatField( verbose_name="Fuel Rate")
    avg_work_truck_mpg  = models.IntegerField( verbose_name="Average Work Truck MPG")
    avg_tower_tech      = models.FloatField( verbose_name="Average Tower Tech Hourly Wage")
    avg_civil_tech      = models.FloatField( verbose_name="Average Civil Tech Hourly Wage")
    loaging_rate        = models.FloatField( verbose_name="Lodging Rate")
    m_i_rate            = models.FloatField( verbose_name="M&I Rate")
    warehouse_log_rate  = models.IntegerField(verbose_name="Warehouse & Log OH Rate (% of Expenses)")
    sg_a_overhead_rate	= models.IntegerField( verbose_name="SG&A Overhead Rate (% of Expenses)")
    desired_margin      = models.IntegerField( verbose_name="Desired Margin")