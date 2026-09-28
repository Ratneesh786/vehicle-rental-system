# vehicles

# module 1:

vehicles = {
    1: {"name": "Swift", "type":"Car","daily_rate": 1500,"available": True},
    2: {"name": "Breeza", "type":"SUV","daily_rate": 2000,"available": True},
    3: {"name": "Baleno", "type":"Car","daily_rate": 1200,"available": True},
    4: {"name": "Creta", "type":"SUV","daily_rate": 2000,"available": True},
    5: {"name": "Fortuner", "type":"SUV","daily_rate": 5000,"available": True},
    6: {"name": "Activa", "type":"Bike","daily_rate": 500,"available": True},
    7: {"name": "Royal Enfield", "type":"Bike","daily_rate": 1200,"available": True},
}

# available type

def available_type(cat):
    return {k:v for k,v in vehicles.items() if v["type"].lower()==cat.lower() and v["available"]}

# available name

def available_name(name):
    for vehicle in vehicles.values():
        if vehicle["name"].lower()==name.lower():
            return vehicle
    return None 

def chg_sts(name,is_avail):
    vehicle = available_name(name)
    if vehicle:
        vehicle["available"] = is_avail