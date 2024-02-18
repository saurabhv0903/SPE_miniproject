FROM ubuntu:latest

# Copy calculator.py and the test file to the /app directory
COPY calculator.py /app/calculator.py
COPY test_calculator.py /app/test_calculator.py
