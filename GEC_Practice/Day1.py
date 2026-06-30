print("Choose an option:")
print("1. Area of Rectangle")
print("2. Arithmetic Operators")
print("3. Arithmetic Progression (Nth Term)")
print("4. Geometric Progression (Nth Term)")
print("5. Compute A Power B")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    print("Area =", l * b)

elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)

    if b != 0:
        print("Division =", a // b)
        print("Modulus =", a % b)
    else:
        print("Division and Modulus are not possible (division by zero).")

elif choice == 3:
    a = int(input("Enter first term: "))
    d = int(input("Enter common difference: "))
    n = int(input("Enter term number: "))

    ans = a + (n - 1) * d
    print("Nth term =", ans)

elif choice == 4:
    a = int(input("Enter first term: "))
    r = int(input("Enter common ratio: "))
    n = int(input("Enter term number: "))

    ans = a * (r ** (n - 1))
    print("Nth term =", ans)

elif choice == 5:
    A = int(input("Enter base: "))
    B = int(input("Enter exponent: "))

    print("Answer =", A ** B)

else:
    print("Invalid Choice")
