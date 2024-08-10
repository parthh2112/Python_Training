

def find_char_length(input_string):
    if not input_string:
        return ""
    
    output_string = ''
    count = 1
    previous = input_string[0]

    for i in range(1,len(input_string)):
        current = input_string[i]
        if current == previous:
            count += 1
        else:
            output_string += previous + str(count)
            count = 1
            previous = current
        
    output_string += previous + str(count)
    return output_string
      


input = "wwwwaaadebbbbbw"
print("Input:", input)
print("Output: ", find_char_length(input))

