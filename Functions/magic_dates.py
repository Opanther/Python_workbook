from day_in_a_month import days


def isMagicDate (day, month, year):
    if day * month == year % 100:
        return True
    return False

def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, days(month, year) + 1):
                if isMagicDate(day, month, year):
                    print("%02d/%02d/%04d is a magic date." % (day, month, year))


if __name__ == "__main__":
    main()