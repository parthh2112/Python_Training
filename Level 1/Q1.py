
print("EXCERCISE 1")
number = int(input("Enter a number: "))
message1= "Consultadd"
message2= "Python Training"
if(number % 3 == 0 and number % 5 == 0):
    print(message1, "-", message2)
elif(number % 3 == 0):
    print(message1)
elif(number % 5 == 0):
    print(message2)
else:
    print("The number is not divisible by 3 or 5.")

    
