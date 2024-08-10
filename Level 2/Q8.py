

def find_number_of_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_count = 0

    for char in string:
        if char in vowels:
            vowels_count += 1

    return vowels_count

string = "Hello, World!"
print("Number of Vowels: ", find_number_of_vowels(string))
