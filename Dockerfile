FROM ubuntu:latest

# Copy calculator.py and the test file to the /app directory
COPY calculator_main.py /app/calculator_main.py
COPY test_calculator_test.py /app/calculator_test.py
