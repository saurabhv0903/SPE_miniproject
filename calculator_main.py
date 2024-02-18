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
    choice = int(input("\nScientific Calculator Menu:\n"
                       "1. Square Root (√x)\n"
                       "2. Factorial (x!)\n"
                       "3. Natural Logarithm (ln(x))\n"
                       "4. Power Function (x^b)\n"
                       "5. Exit\n"
                       "Enter your choice: "))

    if choice == 1:
        sqrt_input = float(input("Enter a number: "))
        print(f"Square Root of {sqrt_input} is: {square_root(sqrt_input)}")

    elif choice == 2:
        factorial_input = int(input("Enter a number: "))
        print(f"Factorial of {factorial_input} is: {factorial(factorial_input)}")

    elif choice == 3:
        log_input = float(input("Enter a number: "))
        print(f"Natural Logarithm of {log_input} is: {natural_log(log_input)}")

    elif choice == 4:
        base = float(input("Enter base (x): "))
        exponent = float(input("Enter exponent (b): "))
        print(f"{base} raised to the power {exponent} is: {power(base, exponent)}")

    elif choice == 5:
        print("Exiting...")

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

