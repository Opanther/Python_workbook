from random import randrange
NUM_ITEMS = 100

mx_values = randrange(1, NUM_ITEMS + 1)
print(mx_values)

num_updates = 0

for i in range(1, NUM_ITEMS):
    current = randrange(1, NUM_ITEMS + 1)

    if current > mx_values:
        mx_values = current
        num_updates += 1
        print(current, "<== Update")
    else:
        print(current)

print("The Maximum value found was", mx_values)
print("The maximum value was updated", num_updates, "times")