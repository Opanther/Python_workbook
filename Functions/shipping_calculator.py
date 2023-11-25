
def ship_cal(items):
    shipping_charge = 10.95
    increment_charge = 2.95

    if items == 1:
        return shipping_charge
    elif items > 1:
        shipping_charge += (items - 1) * increment_charge
        return shipping_charge
    else:
        # Handle the case where the number of items is invalid (less than 1)
        return "Invalid number of items"

def main():
     items = int(input("Enter Number of items in the order: "))
     cost = ship_cal(items)
     print("The cost of shipping for ", items, "items ordered is", cost)

if __name__ == "__main__":
    main()


