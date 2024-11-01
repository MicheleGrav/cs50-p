# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order,
# formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list provided.
# Then output that same date in YYYY-MM-DD format.
# If the user’s input is not a valid date in either format, prompt the user again.
# Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

def main():
    date = get_date("Date: ") # Call function with input prompt
    print(date)

def get_date(prompt):
    while True:
        try:
            date = input(prompt).strip()
            if "/" in date: # Managing standard mont-day-year input
                m, d, y = date.split("/")
                m, d, y = int(m), int(d), int(y)
                if check_days(d) and check_month(m): # Check valid range for day and month numbers
                    return f"{y:04}-{m:02}-{d:02}" # Return in YYYY-MM-DD format
            elif "," in date:
                m, d, y = date.split(" ") # Splitting at the spaces
                d = d.replace(',', '') # Removing the comma that got added in 'day'
                d, y = int(d), int(y)
                m = convert_month(m) # Converting month from literal to numerical
                if check_days(d) and check_month(m):
                    return f"{y:04}-{m:02}-{d:02}" # # Return in YYYY-MM-DD format
        except ValueError:
            pass

# Check valid days range
def check_days(day):
    return 1 <= day <= 31

# Check valid months range
def check_month(month):
    return 1 <= month <= 12

def convert_month(m):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    for i, month in enumerate(months): # Using enumerate() to keep track of both the elements and their indexes
        if m == month:
            return i+1 # 0-based indexing, hence returns i+1
    return None

main()
