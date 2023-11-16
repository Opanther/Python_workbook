new_base = 2
num = int(input("Enter the decimal number:"))
q = num
result = ""

r = q % new_base
result = str(r) + result
q = q //new_base

while q > 0:
    r = q % new_base
    result = str(r) + result
    q = q // new_base

print(f"{num} in decimal is, {result} in binary")
 