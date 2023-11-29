from datetime import datetime

def gregorian_to_ordinal(year, month, day):
    date_object = datetime(year, month, day)
    ordinal_date = date_object.timetuple().tm_yday
    return ordinal_date

def main():
    year = int(input("input the year:"))
    month = int(input("input the month:"))
    day = int(input("input the day:"))
    ordinal_date = gregorian_to_ordinal(year, month, day)
    print(f"The ordinal date for {year}-{month:02d}-{day:02d} is: {ordinal_date}")

if __name__ == "__main__":
    main()

