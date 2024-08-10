
def find_even_length_word(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            even_lwords = [word for word in words if len(word)%2 == 0]
            result = ' '.join(even_lwords)
            return result
    except FileNotFoundError:
            print(f"File '{filename}' not found.")
    except Exception as e:
            print(f"Error: {e}")


file = r"Level 3\doc.txt"
output = find_even_length_word(file)
print(output)

         


