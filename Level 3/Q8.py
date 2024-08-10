

def parse_string(encoded_string):
    first_name = ''
    last_name = ''
    id_no = ''
    parts = encoded_string.split("0")

    parts = [part for part in parts if part]

    first_name = parts[0]
    last_name = parts[1]
    id_no = parts[2]

    decode_dict = {"first_name": first_name,
                   "last_name": last_name,
                   "id": id_no}
    
    return decode_dict

input = "Robert000Smith000123"
print(parse_string(input))