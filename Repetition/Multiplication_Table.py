# Display a multiplication table for 1 times through 10 times 10
Min = 1
Max = 10

#Display the top row of labels
print("    ", end="")
for i in range(Min, Max + 1):
    print("%4d" % i, end="")
print()

for g in range(Min, Max + 1 ):
    print("%4d" % g, end ="")
    for j in range(Min,Max +1):
        print("%4d" % (g*j), end="")
    print()