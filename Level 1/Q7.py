

print("ANAGRAM OF STRING.")

string1 = input("Enter first string: ")
string1  = string1.replace(" ", "").lower()
string2 = input("Enter second string: ")
string2  = string2.replace(" ", "").lower()

print(sorted(string1) == sorted(string2))