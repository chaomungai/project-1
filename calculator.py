def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def find_next_leap_year(start_year):
    """Find the next leap year after the given year."""
    year = start_year + 1
    while not is_leap_year(year):
        year += 1
    return year

def main():
    try:
        user_input = input("Enter a year: ")
        year = int(user_input)

        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")

        next_leap = find_next_leap_year(year)
        print(f"The next leap year after {year} is {next_leap}.")

    except ValueError:
        print("Please enter a valid numeric year (e.g., 2024).")

if __name__ == "__main__":
    main()
