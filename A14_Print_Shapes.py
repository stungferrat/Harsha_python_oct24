def right_angled_triangle(n):
    print("\nRight Angled Triangle:")
    for i in range(1, n + 1):
        print("* " * i)

def equilateral_triangle(n):
    print("\nEquilateral Triangle:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

def square(n):
    print("\nSquare:")
    print(("* " * n + "\n") * n)

def empty_square(n):
    print("\nEmpty Square:")
    print("* " * n)
    for _ in range(n - 2):
        print("*" + "  " * (n - 2) + " *")
    print("* " * n)

def empty_equilateral_triangle(n):
    print("\nEmpty Equilateral Triangle:")
    print(" " * (n - 1) + "*")
    for i in range(1, n - 1):
        print(" " * (n - i - 1) + "*" + "  " * (i - 1) + " *")
    print("* " * n)

def empty_rhombus(n):
    print("\nEmpty Rhombus:")
    print(" " * (n - 1) + "*")
    for i in range(1, n - 1):
        print(" " * (n - i - 1) + "*" + " " * (2 * i - 1) + "*")
    if n > 1:
        print("* " * n)

def hexagon(n):
    print("\nHexagon:")
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (n + i))
    for i in range(1, n):
        print(" " * i + "* " * (2 * n - i - 1))

def x_shape(n):
    print("\nX Shape:")
    for i in range(n):
        print("".join("* " if i == j or i + j == n - 1 else "  " for j in range(n)))

def x_shape_inside_empty_square(n):
    print("\nX Shape Inside Empty Square:")
    for i in range(n):
        print("".join("* " if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or i + j == n - 1 else "  " for j in range(n)))

def pascal_triangle(n):
    print("\nPascal Triangle:")
    for i in range(n):
        print(" " * (n - i), end="")
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()

shapes = {
    "1": square,
    "2": empty_square,
    "3": right_angled_triangle,
    "4": equilateral_triangle,
    "5": empty_equilateral_triangle,
    "6": empty_rhombus,
    "7": hexagon,
    "8": x_shape,
    "9": x_shape_inside_empty_square,
    "10": pascal_triangle
}

print("Select shapes to print by entering numbers (e.g., 1 for Square, 11 for all shapes):")
print("1: Square")
print("2: Empty Square")
print("3: Right Angled Triangle")
print("4: Equilateral Triangle")
print("5: Empty Equilateral Triangle")
print("6: Empty Rhombus")
print("7: Hexagon")
print("8: X Shape")
print("9: X Shape Inside Empty Square")
print("10: Pascal Triangle")
print("11: All Shapes")

choice = input("Enter your choice: ")
n = int(input("Enter the number of lines: "))

if choice == "11":
    for func in shapes.values():
        func(n)
else:
    selected_shapes = choice.split() 
    for ch in selected_shapes:
        if ch in shapes:
            shapes[ch](n)
        else:
            print(f"Invalid choice: {ch}")
