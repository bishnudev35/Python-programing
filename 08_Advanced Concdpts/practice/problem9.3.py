# Create a small program where invalid user input raises a custom exception,
# logs the error, and continues execution instead of crashing.
import logging


class InvalidInputError(Exception):
    pass


while True:
    val = input("Enter a positive number (or 'q' to quit): ")
    if val == "q":
        break

    try:
        num = int(val)
        if num <= 0:
            raise InvalidInputError("Number must be positive!")
        print(f"Valid number: {num}")
    except (ValueError, InvalidInputError) as e:
        logging.error(f"Invalid input: {e}")
        print("Continuing...\n")
