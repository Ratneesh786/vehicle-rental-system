# validity

# module 2:

# days for how much time to rent

def input_days():
    """validity user input to ensure a positive whole integer duration is provided"""
    while True:
        user_input = input("enter rental duration in days: ").strip()

        
        if user_input.isdigit():
            days = int(user_input)
            if days>=1:
                return days
            else:
                 print("[Error] duration must be 1 day or more.")
        else:
            print("[Error]invalid character.please type an integer")
# documents as proof
def input_docs():
    """prevents user from passing empty strings for identification cards"""
    while True:
        docs = input("Provide verification documents").strip()
        if docs!="":
           return docs
        print("[error]documentation details cannot be blank.")

