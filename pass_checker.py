#!/bin/python3
import string
import math
password = input("Enter the password: ")

# Uppercase, Lowercase, Digits and Special character checking 
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])
characters = [upper_case, lower_case, special, digits]
length = len(password)
score = 0

# Common password checking
with open('common.txt', 'r') as f:
	common = f.read().splitlines()
if password in common:
	print ("Invalid Password!")
	print("Password was found in a common list. Score: 0/10")
	print("Password must contain Uppercase, Lowercase, Digits, Special Character")
	exit()
	
# Minimum length checking
if length < 8:
	print ("Invalid Password!")
	print("Minimum length of password is 8. Score: 0/10")
	print("Password must contain Uppercase, Lowercase, Digits, Special Character")
	exit()

# missing_char checking
missing_char1 = ""
missing_char2 = "are missing! Score: 0/10"
if characters[0] == 0:
	missing_char1 += "Uppercase "
if characters[1] == 0:
	missing_char1 += "Lowercase "
if characters[2] == 0:
	missing_char1 += "Special Character "
if characters[3] == 0:
	missing_char1 += "Digits "
if characters[0] == 0 or characters[1] == 0 or characters[2] == 0 or characters[3] == 0:
	print ("Invalid Password!")
	print(missing_char1 + missing_char2)
	print("Password must contain Uppercase, Lowercase, Digits, Special Character")
	exit()
	
# Score setting
if length >= 8:
	score += 1
if length > 10:
	score += 1
if length > 12:
	score += 1
if length > 14:
	score += 1
points = score
	
if sum(characters) > 1:
	score += 1
if sum(characters) > 2:
	score += 1
if sum(characters) > 3:
	score += 1


# entropy calculation:
pool = 0
if characters[0] == 1:
	pool += 26
if characters[1] == 1:
	pool += 26
if characters[2] == 1:
	pool += 32
if characters[3] == 1:
	pool += 10
entropy = length * math.log2(pool)

if score < 4 or length >= 8 and length <= 10 or entropy <=35:
	print(f"The password is quite weak! Score: {str(score)} / 7")
	print(f"Low resistance to Brute Force Attack")
elif score == 4 or length > 10 and length <= 12 or entropy >= 36 and entropy <= 59:
	print(f"The password is ok! Score: {str(score)} / 7")
	print(f"Medium resistance to Brute Force Attack")
elif score > 4 and score < 6 or length > 12 and length <= 14 or entropy >= 60 and entropy <= 119:
	print(f"The password is strong! Score: {str(score)} / 7")
	print(f"High resistance to Brute Force Attack")
elif score > 6 or length > 14 or entropy >= 120:
	print(f"The password is very strong! Score: {str(score)} / 7")
	print(f"Very high resistance to Brute Force Attack")

print(f"Password length is {str(length)}, adding {str(points)} points out of 4!")
print(f"Password ectropy is {str(entropy)}")
