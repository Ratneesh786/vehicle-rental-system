# Design Document

## 1. Project Title

# Vehicle Rental System

The Vehicle Rental System is a Python based console application which
enables a user to select an available vehicle, provide rental details,
perform basic verification and obtain the rental information.
---

# 2. System Overview

The project has been designed as a simple modular Python application.

The application has been split into different files to ensure that
each particular part of the program has a dedicated responsibility.

The files are:
- `main.py`

- `core/vehicles.py` 
- `core/valid.py`
- `core/display.py`
The application begins at `main.py`. The core file takes input from the user
and performs a number of functions in the other modules to complete the rental process.
---
# 3. System Architecture
The project has been built using a simple modular architecture.
```text
+----------------+
|   User   |
+-------+--------+
|
| Input
v
+----------------+
|  main.py   |

| Main Program  |
+-------+--------+
|
+--------------+--------------+
|       |       |
v       v       v
+-------------+ +-------------+ +-------------+
| vehicles.py| |  valid.py | | display.py |
|       | |       | |       |
| Vehicle   | | Input    | | Price and  |
| inventory  | | validation | | receipt   |
+------+------+ +------+------+ +------+------+
|       |       |
+--------------+--------------+
|
v
+----------------+
| Rental Result |
+----------------+
Responsibilities
Module	Responsibility
main.py	Controls the complete user interaction

vehicles.py	Stores vehicle information and handles vehicle searching and availability
valid.py	Validates rental duration and verification documents
display.py	Calculates rental price, security amount and displays the receipt
4. Main User Workflow
The basic workflow of the system is as follows:
START--->Ask for vehicle type--->Find available vehicles--->Are vehicles available?---->+------ NO ------> Show available vehicle types---->+ask for vehicle type again----->YES---->Ask user to select vehicle---->Check vehicle availability--->+------ NOT AVAILABLE ------> Show error---->Yes--->Ask for rental duration--->Validate rental duration--->+------ INVALID ------> Ask again--->VALID--->Ask for verification document--->Validate document--->+------ EMPTY ------> Ask again--->VALID---->Calculate rental amount--->Calculate security amount--->Update vehicle availability--->Print transaction receipt--->END
5. Use Case Design
Actor
The main actor of the system is the Customer/User.
Main Use Cases
Enter vehicle type
View available vehicles
Select a vehicle
Enter rental duration
Provide verification document
Calculate rental amount
Complete the rental process
View transaction receipt
Use Case Representation
+------------------------+
| Vehicle Rental System |
+------------------------+
/   |   \
/   |    \
/    |    \
v    v     v
Enter Vehicle  View Available  Select
Type     Vehicles    Vehicle
\       |       /
\      |       /
\      v      /
---> Enter Rental Days--->Provide Verification
Document--->Calculate Price--->Print Receipt<----Customer
6. Sequence Design
The interaction between the user and the program can be represented as:
Customer    main.py    vehicles.py    valid.py    display.py
|        |        |        |        |
|--vehicle type->|        |        |        |
|        |--search------->|        |        |
|        |<--vehicle list-|        |        |
|<--show list---|        |        |        |
|        |        |        |        |
|--select------>|        |        |        |
|        |--check------->|        |        |
|        |<--availability|        |        |
|        |        |        |        |
|--rental days->|        |        |        |
|        |------------------------------>|        |
|        |<------------------------------|        |
|        |        |        |        |
|--document---->|        |        |        |
|        |------------------------------>|        |
|        |<------------------------------|        |
|        |        |        |        |
|        |----------------------------------------------->|
|        |             Calculate price    |
|        |<-----------------------------------------------|
|<--receipt-----|        |        |        |
|        |        |        |        |
7. Component Design
7.1 vehicles.py
This module contains the vehicle inventory.
Each vehicle contains information such as:
Vehicle name
Vehicle type
Daily rental rate
Availability status
Example vehicle categories in the project are:
Car
SUV
Bike
The module also contains functions for finding vehicles according to their
type or name and changing their availability.
7.2 valid.py
This module is responsible for checking user input.
It contains validation for:
Rental Duration
The user must enter a whole number greater than or equal to one.
If the user enters:
Text instead of a number
Zero
A negative number
the program displays an error and asks for the input again.
Verification Document
The verification document input cannot be empty.
If the user leaves it blank, the program asks for the information again.
7.3 display.py
This module handles the financial information and receipt display.
It calculates:
Rent = Daily Rate × Number of Days
The current implementation also adds a security amount to the rental cost.
The module then prints a formatted transaction receipt containing:
Rented vehicle model
Rent subtotal
Security deposit
Verification document
Grand total
7.4 main.py
main.py works as the main controller of the application.
It:
Starts the rental portal.
Asks the user for a vehicle category.
Gets available vehicles.
Allows the user to select a vehicle.
Calls the validation functions.
Calculates the rental amount.
Updates the vehicle availability.
Prints the final transaction receipt.
8. Data Design
The project uses a Python dictionary as an in-memory data structure.
The basic structure is:
vehicles = {
1: {
"name": "Swift",
"type": "Car",
"daily_rate": 1500,
"available": True
}
}
The important fields are:
Field	Description
name	Name of the vehicle
type	Category of the vehicle
daily_rate	Rental cost for one day
available	Shows whether the vehicle can currently be rented
No external database is used in the current version.
9. Vehicle Categories
The current vehicle inventory contains three main categories:
Cars
Swift
Baleno
SUVs
Breeza
Creta
Fortuner
Bikes
Activa
Royal Enfield
The system filters the inventory according to the category entered by the
user and displays the matching available vehicles.
10. Input and Output Design
Inputs
The system takes the following inputs:
1. Vehicle type
2. Vehicle name
3. Rental duration in days
4. Verification document
Outputs
The system produces:
1. Available vehicle list
2. Error messages for invalid input
3. Rental amount
4. Security amount
5. Transaction receipt
6. Updated vehicle availability
11. Error Handling Design
The system is designed to handle common incorrect inputs.
Invalid Vehicle Type
If the requested category is not available, the program informs the user
and shows the available vehicle categories.
Example:
Sorry, this type is not available.
Available types:
Car
SUV
Bike
The user can then enter another vehicle type.
Invalid Rental Duration
If the user enters an invalid duration, the program displays an error and
asks for the duration again.
Empty Verification Document
If no verification document is entered, the program does not continue and
asks the user to provide the required information.
Vehicle Not Found
If the entered vehicle name does not match an available vehicle, the
program displays an error instead of continuing with an invalid selection.
12. Design Decisions
12.1 Dictionary for Vehicle Storage
A dictionary was selected because the project is a small Python console
application. It makes the vehicle information easy to store, search and
modify.
12.2 Separate Python Modules
The program is divided into different files to make the code easy to
understand and maintain.
For example:
vehicles.py -> Vehicle data and availability
valid.py   -> Input validation
display.py  -> Price and receipt
main.py   -> Main program
12.3 Case-Insensitive Searching
Vehicle type and vehicle name comparisons are handled without depending on
capitalization.
For example:
car
Car
CAR
can represent the same vehicle category.
12.4 Availability Checking
The program checks the availability status before allowing a vehicle to
continue through the rental process.
12.5 Repeated Input
Loops are used where necessary so that an incorrect input does not
immediately terminate the complete program.
13. Price Calculation Design
The rental price is calculated using:
Rent = Daily Rate × Rental Days
The current display.py also adds a security amount to the rent.
The final amount is calculated as:
Grand Total = Rent + Security
The calculated values are then passed to the receipt function.
14. Availability Update
After the rental process is completed, the selected vehicle's availability
is changed.
Conceptually:
Before rental:
available = True--->Rental completed ---->After rental:
available = False
This prevents the same vehicle from being shown as available for another
rental during the current program execution.
15. Overall Design Flow
The complete system can be summarized as:
User--->+Select vehicle type--->Vehicle Inventory--->+Filter available vehicles--->Available Vehicle List--->+Select vehicle--->Vehicle Verification--->+Enter rental days--->Input Validation--->+Enter verification document--->Price Calculation--->Availability Update --->Transaction Receipt--->END
16. Design Summary
The Vehicle Rental System is intentionally designed as a simple console-based
Python application. The main purpose of the design is to keep the program
easy to understand while dividing the work into separate modules.
The design uses:
Python dictionaries for vehicle data
Functions for reusable operations
Conditions for decision making
Loops for repeated input
Separate modules for better organization
Input validation for incorrect values
Availability checking for vehicles
A receipt system for displaying the final transaction