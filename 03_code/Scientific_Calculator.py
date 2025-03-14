import math


def volume_of_shapes():
    shapes = {
        1: ("Sphere", lambda r: (4 / 3) * math.pi * r ** 3, ["radius"]),
        2: ("Cube", lambda a: a ** 3, ["side length"]),
        3: ("Cylinder", lambda r, h: math.pi * r ** 2 * h, ["radius", "height"]),
        4: ("Cone", lambda r, h: (1 / 3) * math.pi * r ** 2 * h, ["radius", "height"]),
        5: ("Rectangular Prism", lambda l, w, h: l * w * h, ["length", "width", "height"]),
        6: ("Pyramid", lambda b, h: (1 / 3) * b * h, ["base area", "height"])
    }

    print("\nChoose a shape to calculate volume:")
    for key, value in shapes.items():
        print(f"{key}. {value[0]}")

    choice = int(input("Enter choice: "))
    if choice in shapes:
        params = [float(input(f"Enter {p}: ")) for p in shapes[choice][2]]
        print(f"Volume: {shapes[choice][1](*params):.2f}")
    else:
        print("Invalid choice")


def solve_equation():
    print("Solving a linear equation of the form: ax + b = 0")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))

    if a == 0:
        if b == 0:
            print("Infinite solutions (any value of x satisfies the equation).")
        else:
            print("No solution (the equation is inconsistent).")
    else:
        x = -b / a
        print(f"Solution: x = {x}")


def square_root():
    num = float(input("Enter number: "))
    print(f"Square Root: {math.sqrt(num)}")


def factorial():
    num = int(input("Enter a positive number: "))
    if num < 0:
        print("Factorial requires a positive number")
        return
    print(f"Factorial: {math.factorial(num)}")


def main():
    options = {
        1: ("Volume of Shapes", volume_of_shapes),
        2: ("Solve Algebraic Equations", solve_equation),
        3: ("Square Root", square_root),
        4: ("Factorial", factorial)
    }

    while True:
        print("\nThe Calculator")
        for key, value in options.items():
            print(f"{key}. {value[0]}")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 5:
            print("Exited The Calculator")
            break
        elif choice in options:
            options[choice][1]()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
