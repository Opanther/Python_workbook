# Reverse Order
data = []

integers = int(input("Enter an integer (enter 0 to finish): "))

while integers != 0:
    data.append(integers)
    integers = int(input("Enter an integer (enter 0 to finish): "))
# sort the reverse in descending order by the setting reverse = True
reverse_sorted_list = sorted(data, reverse=True)

print(reverse_sorted_list)