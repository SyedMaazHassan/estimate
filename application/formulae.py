def TowerHourlyRate(Tower_Personnel, Avg_Tower_Tech):
    if Tower_Personnel >= 4:
        value = 150 + ((Tower_Personnel - 4) * Avg_Tower_Tech)
    else:
        value = 150 - ((4 - Tower_Personnel) * Avg_Tower_Tech)
    
    return {
        "label": "Tower Hourly rate",
        "value": round(value, 2),
        "L": "$"
    }

def CivilHourlyRate(Civil_Personnel, Avg_Civil_Tech):
    if Civil_Personnel >= 3:
        value = 120 + ((Civil_Personnel - 3) * Avg_Civil_Tech)
    else:
        value = 120 - ((3 - Civil_Personnel) * Avg_Civil_Tech)

    return {
        "label": "Civil Hourly rate",
        "value": round(value, 2),
        "L": "$"
    }

def DriveTime(Distance_To_Site):
    return {
        "label": "Drive Time",
        "value": round(Distance_To_Site / 60, 2),
        "R": "unit"
    }
        
def TowerSiteTrips(Is_Perdiem, Expected_Tower_Working_Days):
    if Is_Perdiem == "yes":
        value = 2
    else:
        value = Expected_Tower_Working_Days * 2

    return {
        "label": "Tower Site trips",
        "value": round(value, 2),
    }

def TowerWorkHours(Drive_Time, Tower_Site_Trips, Tower_Working_Days, Tower_Working_Hours):
    value =	(Drive_Time * Tower_Site_Trips) + (Tower_Working_Days * Tower_Working_Hours)
    return {
        "label": "Tower work hours",
        "value": round(value, 2),
    }

def CivilSiteTrips(Is_Perdiem, Days_On_Perdiem, Expected_Civil_Working_Days):
    if Is_Perdiem == "yes":
        value = Expected_Civil_Working_Days - Days_On_Perdiem * 2
    else:
        value = Expected_Civil_Working_Days * 2

    return {
        "label": "Civil site trips",
        "value": round(value, 2),
    }

def CivilWorkHours(drive_time, civil_site_trips, expected_civil_working_days, expected_civil_working_hours):
    value = (drive_time * civil_site_trips) + (expected_civil_working_days * expected_civil_working_hours)
    return {
        "label": "Civil work hours",
        "value": round(value, 2),
    }


def BoxTruckTrips(is_box_trucks_used, distance_to_site):
    value = 0
    if is_box_trucks_used == "yes":
        value = distance_to_site * 2 
    
    return {
        "label": "Box Truck Trips",
        "value": round(value, 2),
    }

def TruckCostPerTrip(truck_per_mile, distance_to_site, tower_trucks, civil_trucks):
    value = truck_per_mile * ((distance_to_site * tower_trucks) + (distance_to_site * civil_trucks))
    return {
        "label": "Truck Cost per trip",
        "value": round(value, 2),
        "L": "$"
    }


def TotalTrailerCost(trailer_per_day, expected_tower_working_days, tower_trailers, expected_civil_working_days, civil_trailers):
    value =	trailer_per_day * (expected_tower_working_days * tower_trailers) + trailer_per_day * (expected_civil_working_days * civil_trailers)
    return {
        "label": "Total trailer Cost",
        "value": round(value, 2),
        "L": "$"
    }


def TargetPrice(target_price):
    value = "N/A"
    if target_price != 0:
        value = target_price
    return {
        "label": "Target price",
        "value": round(value, 2),
        "L": "$"
    }


def RecommendedBidPrice(total_cost, desired_margin):
    value = total_cost / (1 - (desired_margin/100))
    return {
        "label": "Recommended Bid price",
        "value": round(value, 2),
        "L": "$"
    }

def TowerLabor(tower_hourly_rate, tower_work_hours):
    value = tower_hourly_rate * tower_work_hours
    return {
        "label": "Tower Labor",
        "value": round(value, 2),
        "L": "$"
    }

def CivilLabor(civil_hourly_rate, civil_work_hours):
    value = civil_hourly_rate * civil_work_hours
    return {
        "label": "Civil Labor",
        "value": round(value, 2),
        "L": "$"
    }


def TotalTruckCost(tower_site_trips, truck_cost_per_trip):
    value = tower_site_trips * truck_cost_per_trip
    return {
        "label": "Total Truck Cost",
        "value": round(value, 2),
        "L": "$"
    }


def Fuel(fuel_rate, distance_to_site, tower_trucks, tower_site_trips, civil_trucks, civil_site_trips, avg_work_truck_mpg):
    value1 = (fuel_rate * distance_to_site * tower_trucks * tower_site_trips) / avg_work_truck_mpg
    value2 = (fuel_rate * distance_to_site * civil_trucks * civil_site_trips) / avg_work_truck_mpg
    return {
        "label": "Fuel",
        "value": round(value1 + value2, 2),
        "L": "$"
    }

def Perdiem(days_on_perdiem, loaging_rate, m_i_rate, towers_personnel):
    value = days_on_perdiem * (loaging_rate + m_i_rate) * towers_personnel
    return {
        "label": "Perdiem",
        "value": round(value, 2),
        "L": "$"
    }

def TargetPriceNetMargin(target_price, tower_labor, civil_labor, total_truck_cost, total_trailer_cost, fuel, perdiem, sga_overhead_cost, warehouse_log_oh_cost):
    if target_price != "N/A":
        value = ((target_price - tower_labor - civil_labor - total_truck_cost - total_trailer_cost - fuel - perdiem - sga_overhead_cost - warehouse_log_oh_cost) / target_price) * 100
    else:
        value = "N/A"

    return {
        "label": "Target Price Net Margin",
        "value": round(value, 2),
        "R": "%"
    }



def SgaOverheadCost(tower_labor, civil_labor, total_truck_cost, total_trailer_cost, fuel, perdiem, sg_a_overhead_rate):
    value = (tower_labor + civil_labor + total_truck_cost + total_trailer_cost + fuel + perdiem) * (sg_a_overhead_rate / 100)
    return {
        "label": "SG&A Overhead Cost",
        "value": round(value, 2),
        "L": "$"
    }


def WarehouseLogCost(tower_labor, civil_labor, total_truck_cost, total_trailer_cost, fuel, perdiem, warehouse_log_rate):
    value = (tower_labor + civil_labor + total_truck_cost + total_trailer_cost + fuel + perdiem) * (warehouse_log_rate/100)
    return {
        "label": "Warehouse & Log OH Cost",
        "value": round(value, 2),
        "L": "$"
    }

def TotalCost(sga_overhead_cost, warehouse_log_oh_cost, tower_labor, civil_labor, total_truck_cost, total_trailer_cost, fuel, perdiem):
    value = sga_overhead_cost + warehouse_log_oh_cost + tower_labor + civil_labor + total_truck_cost + total_trailer_cost + fuel + perdiem
    return {
        "label": "Total Cost",
        "value": round(value, 2),
        "L": "$"
    }


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

# def TotalTrailerCost(total_trailer_cost):
#     value = total_trailer_cost
#     return {
#         "label": "Total trailer cost",
#         "value": value
#     }  
