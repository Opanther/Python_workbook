# Remove the outliers from a data set
# def removeOutliers(data, num_outliers):
#     return sorted(data)[num_outliers:-num_outliers]

def removeOutliers(data, num_outliers):
    # Create a new copy of the list that is in sorted order
    retval = sorted(data)
    #remove num_outliers largest values
    for i in range(num_outliers):
        retval.pop()

    # remove num_outliers smallest values
    for i in range(num_outliers):
        retval.pop(0)

    return retval

def main():
    values = []
    s = input("Enter a value (blank line to quit) : ")
    while s != "":
        num = float(s)
        values.append(num)
        s = input("Enter a value (blank line to quit) : ")
    if len(values) < 4:
        print("You didn't enter enough values.")
    else:
        print("With the outliers removed: ", removeOutliers(values, 2))
        print("The Original data: ", values)

if __name__ == "__main__":
    main()