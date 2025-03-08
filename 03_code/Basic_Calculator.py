'''
Subject: Basic Calculator of Number_Ninja_code.
Created By: Anup Kumar.
Date: 24-02-2025.
'''

def main():
    try:
        while True:
            print(" 1. Additon \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit ")

            option = int(input("What you want to do: "))
            if (option == 1):
                add()
            elif (option == 2):
                sub()
            elif (option == 3):
                mul()
            elif (option == 4):
                div()
            elif (option == 5):
                exit()
        input("enter any key to continue.....")

    except ValueError:
        print ("\n Invalid input! Please Choose Valid Input \n")


def add():
    try:
        input1 = int(input("How many number you want to Add: "))
        if input1<2:
            temp_1 = float(input("Enter your Number: "))
            print("=", temp_1)
        else:
            temp_1 = float(input("Enter your Number: "))
            temp_2 = float(input("Enter your Number: "))
            total = temp_1 + temp_2
            print("=", total)
            for i in range(input1 - 2):
                number = int(input("Enter your number: "))
                total = number + total
                print("=", total)
    except ValueError:
        print("\n Invalid input! Please enter a valid number... \n")


def sub():
    try:
        input1 = int(input("How many number you want to subtract: "))
        if input1<2:
            temp_1 = float(input("Enter your Number: "))
            print("=", temp_1)
        else:
            temp_1 = float(input("Enter your Number: "))
            temp_2 = float(input("Enter your Number: "))
            total = temp_1 - temp_2
            print("=", total)
            for i in range(input1-2):
                num = float(input("Enter your Number: "))
                total = total - num
                print("=", total)
    except ValueError:
        print("\n Invalid input! Please enter a valid number... \n")


def mul():
    try:
        input1 = int(input("How many number you want to Multiply: "))
        if input1<2:
            temp_1 = float(input("Enter your Number: "))
            print("=", temp_1)
        else:
            temp_1 = float(input("Enter your Number: "))
            temp_2 = float(input("Enter your Number: "))
            total = round((temp_1 * temp_2),2)
            print("=", total)
            for i in range(input1-2):
                number = float(input("Enter your number: "))
                total = number * total
                print("=", total)
    except ValueError:
        print("\n Invalid input! Please enter a valid number... \n")


def div():
    try:
        num_1 = float(input("Enter your number: "))
        num_2 = float(input("Enter your number: "))
        total_1 = num_1 / num_2
        total_2 = num_1 % num_2
        print("Quotient=", total_1)
        print("Remainder=", total_2)
    except ValueError:
        print("\n Invalid input! Please enter a valid number... \n")
    except ZeroDivisionError:
        print("\n Infinity \n")


if __name__ == "__main__":

    main()

    try:
        main()
        add()
        sub()
        mul()
        div()
    except:
        print("!!!Some error happens!!!")