# data = [1.62, 1.41, 3.14, 2.71]
# largest_pos = 0
#
# for i in range(1, len(data)):
#     if data[i] > data[largest_pos]:
#         largest_pos = i
#
# print("The largest value is", data[largest_pos], "which is at index", largest_pos)


data = []

integers = int(input("Enter an integer (enter 0 to finish) :"))

while integers != 0:
    data.append(integers)
    integers = int(input("Enter an integer (enter 0 to finish) :"))
# The list.sort() method in Python sorts the list in place,
# which means it modifies the original list and does not return a new sorted list.
# Therefore, when you write sorted_list = data.sort(), you are
# assigning the result of data.sort() to sorted_list,
# and since data.sort() returns None, sorted_list will also be None.
sorted_list = sorted(data)

print(sorted_list)
