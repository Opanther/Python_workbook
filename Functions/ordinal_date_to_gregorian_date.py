from datetime import datetime, timedelta

def is_leap_year(year):
    # Returns True if the year is a leap year, False otherwise
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def ordinal_to_gregorian(year, ordinal_date):
    # Create a datetime object for January 1st of the specified year
    start_date = datetime(year, 1, 1)

    # Calculate the target date by adding the ordinal number of days minus 1
    target_date = start_date + timedelta(days=ordinal_date - 1)

    # Check if the target date is in a leap year
    if is_leap_year(target_date.year):
        # If the target date is beyond February 28th, adjust for the extra day in leap years
        if target_date.month > 2:
            target_date += timedelta(days=1)

    return target_date

# Example usage:
year = 2024  # Leap year
ordinal_date = 60  # Example ordinal date

gregorian_date = ordinal_to_gregorian(year, ordinal_date)
print(f"The Gregorian date for ordinal date {ordinal_date} in {year} is: {gregorian_date.strftime('%Y-%m-%d')}")