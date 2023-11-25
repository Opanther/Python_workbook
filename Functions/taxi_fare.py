

def taxifare(distance):
    base = 4.00
    extra = distance * 1000 % 140
    total = base + extra * 0.25
    return total
def main():
    distance = int(input("Enter the distance to be calculated in Km: "))
    cost = taxifare(distance)
    print("The cost of the taxi ride is ", cost)

if __name__ == "__main__":
    main()

