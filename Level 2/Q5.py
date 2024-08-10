''' FOR TAKING INPUT FROM USER
temperature_reading = []
k = int(input("Enter number of temperature you want to enter: "))
for i in range(k):
    data = int(input(f"Enter {i} temperature: "))
    temperature_reading.append(data)
'''

temperature_reading = [25, 28, 21, 24, 27]
temperature_avg = sum(temperature_reading)/ len(temperature_reading)
temperature_max = max(temperature_reading)
temperature_min = min(temperature_reading)

print("Average Temperature: ", temperature_avg)
print("Highest Temperature: ", temperature_max)
print("Lowest Temperature: ", temperature_min)