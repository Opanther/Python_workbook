def countrange(data, mn, mx):
    # count the number of elements within the acceptable range
    count = 0
    for i in data:
        # check for each element
        if mn <= i < mx:
            count += 1
    # return the result
    return count


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Test a case where some elements are within the range
    print("Counting the elements in [1..10 between 5 and 7")
    print("Result: %d Expected: 2" % countrange(data, 5, 7))


if __name__ == "__main__":
    main()
