password = input("Enter your password: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check for a number
if any(char.isdigit() for char in password):
    score += 1

# Check for an uppercase letter
if any(char.isupper() for char in password):
    score += 1

# Check for a lowercase letter
if any(char.islower() for char in password):
    score += 1

# Check for a special character
if any(not char.isalnum() for char in password):
    score += 1

# Display score
print("\nPassword Score:", score, "/ 5")

# Display password strength
if score <= 2:
    print("Strength: Weak")
elif score <= 4:
    print("Strength: Medium")
else:
    print("Strength: Strong")
