import string
import os

# Define the base directory and file path for the common passwords list
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'weakpass.txt')

password = input("Enter your password: ")

# Disects the input password into its basic form as a combination of uppercase, lowercase, special characters, and digits 
# Verify the existence of each character type (1 if exists, 0 if not)
UpperC = any([1 if c in string.ascii_uppercase else 0 for c in password])
LowerC = any([1 if c in string.ascii_lowercase else 0 for c in password])
SpecialC = any([1 if c in string.punctuation else 0 for c in password])
Digits = any([1 if c in string.digits else 0 for c in password])

# foundation for password character variety condition checking by returning number of character types inputted by user
pass_char = [UpperC, LowerC, SpecialC, Digits]

# foundation for password length condition checking by returning number of characters inputted by user
pass_length = len(password)

# base score for password strength evaluation, increases with each condition met 
strength_score = 0


# Reads common passwords from the txt file, If file not found, error message is printed and common_pass is initialized as an empty list to avoid program termination and still perform other functions of the password checker despite of it
try:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        common_pass = f.read().splitlines()
except FileNotFoundError:
    print("The file 'weakpass.txt' was not found. Please ensure the file exists in the same directory as this script.")
    common_pass = []  

# Initializes if password inputted is found in common passwords list via the weakpass_4.merged.txt file, which contains a list of common passwords that are easily guessed by hackers.
if password in common_pass:
    print("Password is too common, please create a strong unique and personalized password for maximum security from hackers.")


# Conditions for password strength in length and variety of characters included in the password
if pass_length >= 8:
    strength_score += 1
if pass_length >= 12:
    strength_score += 1
if pass_length >= 15:
    strength_score += 1
if pass_length >= 18:
    strength_score += 1

if sum(pass_char) > 1:
    strength_score += 1
if sum(pass_char) > 2:
    strength_score += 1
if sum(pass_char) > 3:
    strength_score += 1

# Final evaluation of password strength based on conditions met in pass_length and pass_char 
if strength_score < 4:
    print("Weak password, add a unique mix of uppercase/lowercase letters, digits, and special characters.")
elif strength_score == 4:
    print("Sufficient password, consider adding more characters for uniqueness and safety purposes.")
elif 4 < strength_score < 7:
    print("Moderately strong password, but could be improved with additional characters and complexity.")
elif strength_score >= 7:
    print("Strong password!, Filled the minimum requirements. Note that the password should be different across multiple accounts for safety and security purposes.")


