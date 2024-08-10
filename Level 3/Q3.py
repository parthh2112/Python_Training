

def JtoI(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            correct_content = content.replace("J", "I")
        print(correct_content)

    except FileNotFoundError:
        print(f"Error: File: '{filename}' not found.")
    
    except Exception as e:
        print(f"Error: {e}")

file = r"Level 3\words.txt"
JtoI(file)
