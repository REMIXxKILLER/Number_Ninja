'''Created on: 5-03-2025
Created by: Moumita
Objective:1. Advanced calculator project
'''
import math

#Function for simple interest
def simple_interest():
    #take inputs from the customer
    principal = float(input("Enter the Principal amount: "))
    rate = float(input("Enter rate of interest per annum: "))
    time = float(input("Enter the total time in years: "))

    #Formula for simple interest
    SI = math.floor (principal * rate * time) /100

    #Total amount including interest
    amount = principal + SI

    print("Total interest paid after ",time ,"years= ", SI)
    print("Total amount received with interest: ", amount)

#Function for compound interest
def compound_interest():

    #Enter details from the user
    principal =float(input("Enter the Principal amount: "))
    rate = float(input("Enter rate of interest per annum: "))
    time = float(input("Enter the total time in years: "))

    #Formula to find the total amount with interest
    amount = math.floor (principal * (pow ((1+ rate / 100), time)))

    #Formula to find only interest value
    CI = amount - principal
    print("Total amount paid after ",time ,"years= ",amount)
    print("Compound interest is : ",CI)

if __name__ == "__main__":
    try:
        print("Welcome to our Banking system","\n")
        while True:
            print("1) Simple Interest", "2) Compound Interest","3) Exit", sep = "\n")
            option = int(input("Enter your choice:"))
            if option == 1:
                simple_interest()
            elif option == 2:
                compound_interest()
            elif option == 3:
                exit()
            else:
                print("Please enter a valid choice")
    except:
        print("Technical Issue")

    finally:
        print("\n","Thank you")











