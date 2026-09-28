# display
# module 3:

# available items

def print_catalog(available_items,category):
     print(f"\n=====AVAILABLE{category.upper()}OPTIONS=====")
     index=1
     for item in available_items.values():
          print(f"[{index}].{item['name']} | Price: RS.{item['daily_rate']}/days")
          index+=1

# daily rate and security

def price(daily_rate,days):
    rent=daily_rate*days
    security=3000
    total=rent+security
    return {
        "rent": rent,
        "security": security,
        "total": total
        }

# receipt
def print_receipt(name,days,costs,paperwork):
    """final formatted transaction receipt."""
    print("\n"+"="*15+"TRANSACTION RECEIPT" + "="*15 )
    print(f"Rented Model: {name}")
    print(f"Rent Subtotal: Rs.{costs['rent']}")
    print(f"Security Deposit: Rs.{costs['security']}")
    print(f" Logged Document:  {paperwork}")
    print("-" * 46)
    print(f" GRAND TOTAL PAID: Rs. {costs['total']}")
    print("=" * 46)
    print("Process complete. Drive safe!\n")