'''
objective: conversation
created by:- Gourav Kar
date:-
'''
import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

def kilometer_to_meter(kilometers):
    return kilometers * 1000

def meter_to_centimeter(meters):
    return meters * 100

def conversion_calculator():
    while True:
        print("""
Select conversion:
1. Degrees to Radians
2. Kilometer to Meter
3. Meter to Centimeter
        """)

        try:
            choice = input("Enter choice (1/2/3): ")

            if choice == '1':
                degrees = float(input("Enter degrees: "))
                radians = degrees_to_radians(degrees)
                print("Degrees:-",degrees , "\n"  "Radians:--", round(radians,2))
            elif choice == '2':
                kilometers = float(input("Enter kilometers: "))
                meters = kilometer_to_meter(kilometers)
                print("Kilometers:-",kilometers , "\n"  "Meter:--", round(meters,2))
            elif choice == '3':
                meters = float(input("Enter meters: "))
                centimeters = meter_to_centimeter(meters)
                print("Meter:-",centimeters , "\n"  "Centimeters--", round(centimeters,2))
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    conversion_calculator()
