# main.py

import core.vehicles as inventory
import core.valid as validation
import core.display as display

# initialization

def initialize_booking():
    print("--- Vehicle Rental Portal ---")
    
    
    category = input("What type of ride do you want? (Car/SUV/Bike): ").strip()
    available_stock = inventory.available_type(category)
    
    if not available_stock:
        print(f"No available {category}s found inside system registries.")
        return
        
    display.print_catalog(available_stock, category)
    
    # selecting the vehicle
    
    selection = input("\nType the exact name of the model to select: ").strip()
    vehicle = inventory.available_name(selection)
    
    if not vehicle or not vehicle["available"]:
        print("[Error] Model not found or currently checked out.")
        return
        
    # validation

    paperwork = validation.input_docs()
    days = validation.input_days()
    
    # invoice

    invoice_costs = display.price(vehicle["daily_rate"], days)
    inventory.chg_sts(vehicle["name"], is_avail=False)
    
    # display

    display.print_receipt(vehicle["name"], days, invoice_costs, paperwork)

# name

if __name__ == "__main__":
    initialize_booking()