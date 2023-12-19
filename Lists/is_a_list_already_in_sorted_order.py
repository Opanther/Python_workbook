def is_list_sorted(data):
    if not data:
        return None  # Indicates an empty list
    for i in range(1, len(data)):
        if data[i - 1] > data[i]:
            return False
    return True


def main():
    data = []

    integers = int(input("Enter an integer (enter blank to finish) :"))

    while integers != "":
        if integers:
            data.append(int(integers))
        integers = input("Enter an integer (enter blank to finish) :")

    sorted = is_list_sorted(data)

    if sorted is None:
        print("Please enter at least one integer.")
    elif sorted:
        print("The list is sorted.")
    else:
        print("The list is not sorted.")


if __name__ == "__main__":
    main()
