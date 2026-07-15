import datetime
from typing import Optional


def prompt_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def prompt_int(prompt: str, min_value: Optional[int] = None, max_value: Optional[int] = None) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if min_value is not None and value < min_value:
            print(f"Please enter a value greater than or equal to {min_value}.")
        elif max_value is not None and value > max_value:
            print(f"Please enter a value less than or equal to {max_value}.")
        else:
            return value


def prompt_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    print("Welcome to the Interactive Personal Data Collector!")
    print()

    name = prompt_non_empty("Please enter your name: ")
    age = prompt_int("Please enter your age: ", min_value=0, max_value=130)
    height = prompt_float("Please enter your height in meters: ")
    number = prompt_int("Please enter your favourite number: ")

    print()
    print("Thank you! Here is the information we collected:")
    print()

    print(f"Name: {name} (type: {type(name).__name__}, memory address: {id(name)})")
    print(f"Age: {age} (type: {type(age).__name__}, memory address: {id(age)})")
    print(f"Height: {height} (type: {type(height).__name__}, memory address: {id(height)})")
    print(f"Favourite Number: {number} (type: {type(number).__name__}, memory address: {id(number)})")

    print()

    current_year = datetime.datetime.now().year
    birth_year = current_year - age
    print(f"Your birth year is approximately: {birth_year} (based on your age of {age})")

    print()
    print("Thank you for using the Personal Data Collector. Goodbye!")


if __name__ == "__main__":
    main()
