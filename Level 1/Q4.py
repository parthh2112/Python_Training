print("EXCERCISE 4")

start = int(input("Enter starting number : "))
end = int(input("Enter stopping number: "))
total = 0

if start % 2 == 0:
    start += 1
    
for i in range(start,end,2):
    total += i

print(f"Sum of odd numbers : {total}")