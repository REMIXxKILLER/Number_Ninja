'''
objective: trignometry(sin,cos,tan)
created by:- Gourav Kar
date:-
'''
import math

def trigonometry():
    print("""
Select function:
1. Sine
2. Cosine
3. Tangent
4. Cotangent
5. Cosecant
6. Secant
7. Exit
    """)

    try:
        while True:
            choice = input("Enter choice:: ")

            if choice == '7':  # Exit option
                print("Exiting the calculator. Goodbye!")
                break

            angle = float(input("Enter angle in degrees:: "))
            radians = math.radians(angle)  # Convert angle from degrees to radians

            if choice == '1':
                print("Sin(", angle, ") =", round(math.sin(radians), 2))
            elif choice == '2':
                print("Cos(", angle, ") =", round(math.cos(radians), 2))
            elif choice == '3':
                print("Tan(", angle, ") =", round(math.tan(radians), 2))
            elif choice == '4':
                try:
                    cot_value = 1 / math.tan(radians)
                    print("Cot(", angle, ") =", round(cot_value, 2))
                except ZeroDivisionError:
                    print("Cotangent is undefined for angles")
            elif choice == '5':
                try:
                    csc_value = 1 / math.sin(radians)
                    print("Cosec(", angle, ") =", round(csc_value, 2))
                except ZeroDivisionError:
                    print("Cosecant is undefined for angles where sine is zero")
            elif choice == '6':
                try:
                    sec_value = 1 / math.cos(radians)
                    print("Sec(", angle, ") =", round(sec_value, 2))
                except ZeroDivisionError:
                    print("Secant is undefined for angles where cosine is zero")
            else:
                print("Invalid choice.")
    except ValueError:
        print("Invalid input! Please enter numeric values only.")

# Main function
if __name__ == "__main__":
    # Run the trigonometry calculator
    trigonometry()

