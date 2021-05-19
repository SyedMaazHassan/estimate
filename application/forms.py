from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *


class estimateForm(forms.ModelForm):
    class Meta:
        model = estimate_inputs
        fields = [
            "current_date",
            "construnction_start_date",
            "target_price",
            "carrier",
            "landlord",
            "turf_vendor",
            "site_name",
            "latitude",
            "longitude",
            "is_tower_work",
            "towers_personnel",
            "expected_tower_working_days",
            "expected_tower_working_hours",
            "tower_trucks",
            "tower_trailers",
            "is_civil_work",
            "civil_personnel",
            "expected_civil_working_days",
            "expected_civil_working_hours",
            "civil_trucks",
            "civil_trailers",
            "is_box_trucks_used",
            "box_trcuk_utilization",
            "is_perdiem",
            "expected_perdiem_working_days",
            "days_on_perdiem",
            "distance_to_site"
        ]

    def get_fields(self):
        return self.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label_dict = {
            "current_date": "Today's Date / Date of Estimate",
            "construnction_start_date": "Anticipated Construction Start Date",
            "target_price": "Target Pricing (If Any)",
            "carrier": "What carrier is this site for?",
            "landlord":	"Who is the landlord",
            "turf_vendor": "Turf Vendor",
            "site_name": "Site Name",
            "latitude":	"Latitude",
            "longitude": "Longitude",
            "is_tower_work": "Will there be tower work on this site?",
            "towers_personnel":	"Number of Tower Personnel",
            "expected_tower_working_days": "Number of expected tower work days",
            "expected_tower_working_hours":	"Number of expected tower hours per work day (On Site)",
            "tower_trucks":	"Number of trucks used for tower personnel",
            "tower_trailers": "Number of trailers used for tower personnel",
            "is_civil_work": "Will there be civil work on this site?",
            "civil_personnel": "Number of Civil Personnel",
            "expected_civil_working_days": "Number of expected civil work days",
            "expected_civil_working_hours":	"Number of expected civil hours per work day (On Site)",
            "civil_trucks": "Number of trucks used for civil personnel",
            "civil_trailers": "Number of trailers used for civil personnel",
            "is_box_trucks_used": "Will a box truck be used on site?",
            "box_trcuk_utilization": "How will the box truck be utilized?",
            "is_perdiem": "Will there be any perdiem on this site?",
            "expected_perdiem_working_days": "How many days will there be perdiem on this site?",
            "days_on_perdiem": "How many days on perdiem?",
            "distance_to_site":	"Distance to Site"
        }

        for key, label in label_dict.items():
            self.fields[key].label = label

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))



class base_valuesForm(forms.ModelForm):
    class Meta:
        model = base_values
        fields = [
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

    def get_fields(self):
        return self.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label_dict = {
            "site_number":	"Site number",
            "truck_per_mile":	"Truck Per Mile",
            "trailer_per_day":	"Trailer Per Day",	
            "fuel_rate":	"Fuel Rate",
            "avg_work_truck_mpg":	"Average Work Truck MPG",
            "avg_tower_tech":	"Average Tower Tech Hourly Wage",
            "avg_civil_tech":	"Average Civil Tech Hourly Wage",
            "loaging_rate":	"Lodging Rate",
            "m_i_rate":	"M&I Rate",
            "warehouse_log_rate":	'Warehouse & Log OH Rate (% of Expenses)',
            "sg_a_overhead_rate":	'SG&A Overhead Rate (% of Expenses)',
            "desired_margin":	"Desired Margin	integer"
        }
        
        for key, label in label_dict.items():
            self.fields[key].label = label

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

