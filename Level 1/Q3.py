print("EXCERCISE 3")

Physics = int(input("Enter Physics Marks: "))
Chemistry = int(input("Enter Chemistry Marks: "))
Biology = int(input("Enter Biology Marks: "))
Mathematics = int(input("Enter Mathematics Marks: "))
Computer = int(input("Enter Computer Marks: "))
percentage = (Physics + Chemistry + Biology + Mathematics + Computer)/5
print(percentage)

if percentage>= 90:
    print("Grade A")
elif percentage>= 80:
    print("Grade B")
elif percentage>= 70:
    print("Grade C")
elif percentage>= 60:
    print("Grade D")
elif percentage>= 40:
    print("Grade E")
else:
    print("Grade F")