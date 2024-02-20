FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

USER jenkins

# Copy calculator.py and the test file to the /app directory
COPY calculator_main.py /app/calculator_main.py
COPY calculator_test.py /app/calculator_test.py
