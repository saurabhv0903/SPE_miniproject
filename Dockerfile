FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Copy calculator.py and the test file to the /app directory
COPY calculator_main.py /app/calculator_main.py
COPY calculator_test.py /app/calculator_test.py


# CMD printf "1\n4\n3\n" | python3 calculator_main.py
CMD ["python3",  "calculator_main.py"]
