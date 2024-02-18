import sys
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
    if len(sys.argv) < 3:
        print("Usage: python3 calculator_main.py <option> <value>")
        print("Options:")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power Function (x^b)")
        sys.exit(1)

    option = int(sys.argv[1])
    value = float(sys.argv[2])

    if option == 1:
        print("Square Root of", value, "is:", square_root(value))
    elif option == 2:
        print("Factorial of", value, "is:", factorial(int(value)))
    elif option == 3:
        print("Natural Logarithm of", value, "is:", natural_log(value))
    elif option == 4:
        if len(sys.argv) < 4:
            print("Usage: python3 calculator_main.py 4 <base> <exponent>")
            sys.exit(1)
        exponent = float(sys.argv[3])
        print(value, "raised to the power", exponent, "is:", power(value, exponent))
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()
