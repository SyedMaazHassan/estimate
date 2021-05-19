# from typing_extensions import Required
from webapp.settings import STATIC_ROOT
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .forms import *
from .formulae import *
# main page function

def check_site(request):
    output = {'status': False}
    if request.method == "GET" and request.is_ajax():
        site_name = request.GET['site_name']
        if base_values.objects.filter(site_number = site_name).exists():
            output['status'] = True

    return JsonResponse(output)

def Merge(dict1, dict2):
    return(dict2.update(dict1))

def formulate_parameters(dictionary):
    towers_personnel = int(dictionary['towers_personnel'])
    avg_tower_tech = dictionary['avg_tower_tech']
    civil_personnel = dictionary['civil_personnel']
    avg_civil_tech = dictionary['avg_civil_tech']
    distance_to_site = dictionary['distance_to_site']
    is_perdiem = dictionary['is_perdiem']
    expected_tower_working_days = dictionary['expected_tower_working_days']
    expected_tower_working_hours = dictionary['expected_tower_working_hours']
    days_on_perdiem = dictionary['days_on_perdiem']
    expected_civil_working_days = dictionary['expected_civil_working_days']
    expected_civil_working_hours = dictionary['expected_civil_working_hours']
    is_box_trucks_used = dictionary['is_box_trucks_used']
    truck_per_mile = dictionary['truck_per_mile']
    tower_trucks = dictionary['tower_trucks']
    civil_trucks = dictionary['civil_trucks']
    trailer_per_day = dictionary['trailer_per_day']
    tower_trailers = dictionary['tower_trailers']
    civil_trailers = dictionary['civil_trailers']
    target_price = dictionary['target_price']
    desired_margin = dictionary['desired_margin']
    avg_work_truck_mpg = dictionary['avg_work_truck_mpg']
    fuel_rate = dictionary['fuel_rate']
    loaging_rate = dictionary['loaging_rate']
    m_i_rate = dictionary['m_i_rate']
    sg_a_overhead_rate = dictionary['sg_a_overhead_rate']
    warehouse_log_rate = dictionary['warehouse_log_rate']
    

    # Admin output
    tower_hourly_rate       = TowerHourlyRate(towers_personnel, avg_tower_tech)
    civil_hourly_rate       = CivilHourlyRate(civil_personnel, avg_civil_tech)
    drive_time              = DriveTime(distance_to_site)
    tower_site_trips        = TowerSiteTrips(is_perdiem, expected_tower_working_days)
    tower_work_hours        = TowerWorkHours(drive_time['value'], tower_site_trips['value'], expected_tower_working_days, expected_tower_working_hours)
    civil_site_trips        = CivilSiteTrips(is_perdiem, days_on_perdiem, expected_civil_working_days)
    civil_work_hours        = CivilWorkHours(drive_time['value'], civil_site_trips['value'], expected_civil_working_days, expected_civil_working_hours)
    box_truck_trips         = BoxTruckTrips(is_box_trucks_used, distance_to_site)
    truck_cost_per_trip     = TruckCostPerTrip(truck_per_mile, distance_to_site, tower_trucks, civil_trucks)
    total_trailer_cost      = TotalTrailerCost(trailer_per_day, expected_tower_working_days, tower_trailers, expected_civil_working_days, civil_trailers)
    
    # User output
    target_price_2          = TargetPrice(target_price)
    tower_labor             = TowerLabor(tower_hourly_rate['value'], tower_work_hours['value'])
    civil_labor             = CivilLabor(civil_hourly_rate['value'], civil_work_hours['value'])
    total_truck_cost        = TotalTruckCost(tower_site_trips['value'], truck_cost_per_trip['value'])
    total_trailer_cost_2    = total_trailer_cost
    fuel                    = Fuel(fuel_rate, distance_to_site, tower_trucks, tower_site_trips['value'], civil_trucks, civil_site_trips['value'], avg_work_truck_mpg)
    perdiem                 = Perdiem(days_on_perdiem, loaging_rate, m_i_rate, towers_personnel)
    sga_overhead_cost_2     = SgaOverheadCost(tower_labor['value'], civil_labor['value'], total_truck_cost['value'], total_trailer_cost['value'], fuel['value'], perdiem['value'], sg_a_overhead_rate)
    warehouse_log_oh_cost_2 = WarehouseLogCost(tower_labor['value'], civil_labor['value'], total_truck_cost['value'], total_trailer_cost['value'], fuel['value'], perdiem['value'], warehouse_log_rate)
    total_cost              = TotalCost(sga_overhead_cost_2['value'], warehouse_log_oh_cost_2['value'], tower_labor['value'], civil_labor['value'], total_truck_cost['value'], total_trailer_cost['value'], fuel['value'], perdiem['value'])
    recommended_bid_price   = RecommendedBidPrice(total_cost["value"], desired_margin)
    target_price_net_margin = TargetPriceNetMargin(target_price, tower_labor['value'], civil_labor['value'], total_truck_cost['value'], total_trailer_cost['value'], fuel['value'], perdiem['value'], sga_overhead_cost_2['value'], warehouse_log_oh_cost_2['value'])

    output = {
        "admin": [
            tower_hourly_rate,
            civil_hourly_rate,
            drive_time,
            tower_site_trips,
            tower_work_hours,
            civil_site_trips,
            civil_work_hours,
            box_truck_trips,
            truck_cost_per_trip,
            total_trailer_cost, 
        ],
        "user": [
            target_price_2,
            tower_labor,
            civil_labor,
            total_truck_cost,
            total_trailer_cost_2,
            fuel,
            perdiem,
            sga_overhead_cost_2,
            warehouse_log_oh_cost_2,
            total_cost,
            recommended_bid_price,
            target_price_net_margin
        ] 
    }
    # print(output)
    return output

def get_estimate(request):
    context = {}
    if request.method == "POST":
        site_name = request.POST['site_name']
        base_values_query = base_values.objects.filter(site_number = site_name)
        if base_values_query.exists():
            base_values_query = model_to_dict(base_values_query[0])
            # print(base_values_query)
            form_data = estimateForm(request.POST)
            if form_data.is_valid():
                form_data.save()
                new_record = list(estimate_inputs.objects.all())[-1]
                return redirect("result", id = new_record.id)
        else:
            messages.info(request, "Entered site doesn't exists!")

    return render(request, "result.html", context)


def result(request, id):
    input_object_query = estimate_inputs.objects.filter(id = id)
    if input_object_query.exists():
        input_object = model_to_dict(input_object_query[0])
        base_values_query = base_values.objects.filter(site_number = input_object['site_name'])
        if base_values_query.exists():
            base_value = model_to_dict(base_values_query[0])
            dictionary = {**input_object, **base_value}
            results = formulate_parameters(dictionary)
            
            my_list = []
            
            for key, value in label_dict.items():
                temp_tuple = (
                    value,
                    input_object[key]
                )
                my_list.append(temp_tuple)

            context = {
                'results': results,
                'inputs': my_list,
            }
            return render(request, "result.html", context)
        else:
            return redirect("index")
    else:
        return redirect("index")


def history(request):
    all_inputs = list(estimate_inputs.objects.all())[::-1]
    context = {
        'all_estimates': all_inputs
    }
    return render(request, "history.html", context)

def index(request):
    form_class = estimateForm()
    context = {
        'form': form_class,
        'fields': form_class.get_fields()
    }
    return render(request, 'main.html', context)

# function for signup
def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        l_name = request.POST['l_name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        context = {
            "name":name,
            "l_name":l_name,
            "email":email,
            "pass1":pass1,
            "pass2":pass2,
        }
        if pass1==pass2:
            if User.objects.filter(username=email).exists():
                print("Email already taken")
                messages.info(request, "Entered email already in use!")
                context['border'] = "email" 
                return render(request, "signup.html", context)

            user = User.objects.create_user(username=email, first_name=name, password=pass1, last_name=l_name)
            user.save()
            
            return redirect("login")
        else:
            messages.info(request, "Your pasword doesn't match!")
            context['border'] = "password"
            return render(request, "signup.html", context)


    
    return render(request, "signup.html")


# function for login

def login(request):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        context = {
            'email': email,
            'password': password
        }
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Incorrect login details!")
            return render(request, "login.html", context)
            # return redirect("login")
    else:
        return render(request, "login.html")


# function for logout

def logout(request):
    auth.logout(request)
    return redirect("index")

