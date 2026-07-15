print("Welcome to the Interactive Personal Data Collector!")

print(" ")

import datetime

name=input("Please enter your name: ")
age=int(input("Please enter your age: "))
height=float(input("Please enter your height: "))
number=int(input("Please enter your favourite number: "))

current_year = datetime.datetime.now().year
birth_year = current_year - age

print(" ")

print("Thank you! Here is the information we collected:")

print(" ")

print(f"Name: {name} (type: {type(name)} Memory Address: {id(name)})")
print(f"Age: {age} (type: {type(age)} Memory Address: {id(age)})")
print(f"Height: {height} (type: {type(height)} Memory Address: {id(height)})")
print(f"Favourite Number: {number} (type: {type(number)} Memory Address: {id(number)})")

print(" ")

current_year = datetime.datetime.now().year
birth_year = current_year - age

print(f"Your birth year is approximately: {birth_year} (based on your age of {age})")

print(" ")

print("Thank you for using the Personal Data Collector. Goodbye!")
        