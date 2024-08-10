

def uniq_element(list_of_num):
    uniq = []
    seen = []

    for num in list_of_num:
        if num not in seen:
            uniq.append(num)
            seen.append(num)

    return uniq

list1 = [1, 2, 2, 3, 4, 4, 5, 5]

print("Orignal List: ", list1)
print("Unique List: ", uniq_element(list1))