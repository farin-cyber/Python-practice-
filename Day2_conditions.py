# Day 2 - Conditions

# 1. Check if a number is positive, negative or zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 2. Check whether someone is an adult or minor
age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# 3. Check whether a number is even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
