
import string

print("Excercise 2")
userMessage = input("Enter Anything: ")
alpha = 0
num = 0

#First WAY
small_alphabate = list(string.ascii_lowercase) 
capital_alphabate = list(string.ascii_uppercase)
alphabate = small_alphabate + capital_alphabate
digits = list(string.digits)


for i in userMessage:
    if i in alphabate:
        alpha += 1
    if i in digits:
        num += 1

print(f"Alphabets: {alpha} & Number : {num}")

#SECOND WAY
alpha = 0
num = 0

for i in userMessage:
    if i.isalpha():
        alpha += 1
    if i.isdigit():
        num += 1

print(f"Alphabets: {alpha} & Number : {num}")
    


