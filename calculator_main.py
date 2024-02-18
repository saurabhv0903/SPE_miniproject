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
        print("Usage: python3 calculator_main.py <operation> <value>")
        print("Operations:")
        print("1. Square Root (√x): sqrt")
        print("2. Factorial (x!): factorial")
        print("3. Natural Logarithm (ln(x)): log")
        print("4. Power Function (x^b): power")
        sys.exit(1)

    operation = sys.argv[1]
    value = float(sys.argv[2])

    if operation == 'sqrt':
        print("Square Root of", value, "is:", square_root(value))
    elif operation == 'factorial':
        print("Factorial of", value, "is:", factorial(int(value)))
    elif operation == 'log':
        print("Natural Logarithm of", value, "is:", natural_log(value))
    elif operation == 'power':
        if len(sys.argv) < 4:
            print("Usage: python3 calculator_main.py power <base> <exponent>")
            sys.exit(1)
        exponent = float(sys.argv[3])
        print(value, "raised to the power", exponent, "is:", power(value, exponent))
    else:
        print("Invalid operation!")

if __name__ == "__main__":
    main()
