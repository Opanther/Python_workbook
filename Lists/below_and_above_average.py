values = []
lower = []
higher = []

line = input("Enter an Integer (blank line to quit): ")
while line != "":
    line = int(line)
    values.append(line)

    line = input("Enter an Integer (blank line to quit): ")

mean = round(sum(values)/ len(values))

for i in values:
    if i > mean:
        higher.append(i)
    elif i < mean:
        lower.append(i)

print(f"The average of the values entered {mean} ")
print(f"Th value(s) below the average is {lower} ")
print(f"Th value(s) above the average is {higher} ")