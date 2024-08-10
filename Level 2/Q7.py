

def find_median(list_number):
    list_number.sort()
    n = len(list_number)
    if n % 2 == 0:
        mid1 = list_number[(n//2) - 1]
        mid2 = list_number[n//2]
        median = (mid1 + mid2) / 2.0
        
    else:
        median = number_list[n // 2]
    return median



number_list = [7, 2, 5, 1, 9, 3]
print("Median is: ", find_median(number_list))