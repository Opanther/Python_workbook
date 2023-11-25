def median(a, b, c):
    values_sort = [a,b,c]
    sort_value = sorted(values_sort)
    median_value =sort_value[1]
    return median_value

def main():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    c = float(input("Enter the third value: "))
    value = median(a,b,c)
    print("The median of the values is", value)

if __name__ == "__main__":
    main()
