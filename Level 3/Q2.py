

def count_liens(filename):
    line_count = 0 
    try:
        with open(filename, 'r') as file:
            for line in file:
                line_count += 1
            return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

file = r"Level 3\demo.txt"
line_count = count_liens(file)
if line_count is not None:
    print(f"Number of lines in 'demo.txt': {line_count}")

