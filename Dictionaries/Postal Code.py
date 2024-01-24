postal_code = {
    'A': 'Newfoundland', 'B': 'Nova Scotia', 'C': 'Prince Edward Island', 'E': 'New Brunswick',
    'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec',
    'K': 'Ontario', 'L': 'Ontario', 'M': 'Ontario', 'N': 'Ontario', 'P': 'Ontario',
    'R': 'Manitoba', 'S': 'Saskatchewan', 'T': 'Alberta',
    'V': 'British Columbia', 'X': 'Nunavut or Northwest Territories', 'Y': 'Yukon'
}

def postcode_check(addres):
    if addres[0] not in postal_code or not addres[1].isdigit():
        return "Invalid postal code"
    elif addres[1] == '0':
        return f"This postal code is for a rural address in {postal_code[addres[0]]}"
    else:
        return f"This postal code is for an urban address in {postal_code[addres[0]]}"


user_input = input("Enter a postcode: ").upper()

result = postcode_check(user_input)

print(result)