import math

def square_root(x):
    return math.sqrt(x)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def natural_log(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def main():
    print("Options:")
    print("1. Square Root (√x)")
    print("2. Factorial (x!)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power Function (x^b)")

    option = int(input("Enter your option: "))
    value = float(input("Enter the value: "))

    if option == 1:
        print("Square Root of", value, "is:", square_root(value))
    elif option == 2:
        print("Factorial of", value, "is:", factorial(int(value)))
    elif option == 3:
        print("Natural Logarithm of", value, "is:", natural_log(value))
    elif option == 4:
        exponent = float(input("Enter the exponent: "))
        print(value, "raised to the power", exponent, "is:", power(value, exponent))
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()

