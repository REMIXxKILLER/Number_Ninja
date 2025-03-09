'''
objective: trignometry(sin,cos,tan)
created by:- Gourav Kar
date:-
'''
# import math
# def trigonometry() :
#     print( """
# Select function:
# 1. Sine
# 2. Cosine
# 3. Tangent
# 4.
#     """ )
#
#     try :
#         while True :
#             choice = input( "Enter choice (1/2/3): " )
#             angle = float( input( "Enter angle in degrees:==  " ) )
#             radians = math.radians( angle )  # Convert angle x from degrees to radians
#             if choice == '1' :
#                 print("Sin=", angle , "is=", math.sin(radians))
#             elif choice == '2' :
#                 print("cos=", angle , "is=", math.cos(radians))
#             elif choice == '3' :
#                 print("Tan=", angle , "is=", math.tan(radians))
#             else :
#                 print( "Invalid choice." )
#
#     except ValueError :
#         input( "Invalid input! Please enter numeric values only." )
#
# # Run the trigonometry calculator
# trigonometry()

import math

def trigonometry():
    print("""
Select function:
1. Sine
2. Cosine
3. Tangent
4. Cotangent
    """)

    try:
        while True:
            choice = input("Enter choice:: ")
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
                    print("Cotangent is undefined for angles ")
            else:
                print("Invalid choice.")
    except ValueError:
        print("Invalid input! Please enter numeric values only.")

# Main function
if __name__ == "__main__":
    # Run the trigonometry calculator
    trigonometry()
