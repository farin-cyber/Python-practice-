# Day 1 - Python Basics

# Variables and Data Types
name = "Farin"
age = 19

print(name)
print(age)

# Taking Input
user_age = int(input("Enter your age: "))
print("Your age is:", user_age)

# Arithmetic Operators
x = 10
y = 3

print("Addition:", x + y)
print("Floor Division:", x // y)

# Positive, Negative or Zero
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Assignment vs Comparison
a = 10       # Assignment
print(a == 10)  # Comparison
