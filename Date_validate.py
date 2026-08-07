
from datetime import datetime

def validate_date():
    while True:
        date = input("Enter date (DD-MM-YYYY): ")
        try:
            return datetime.strptime(date, "%d-%m-%Y").isoformat()
        except ValueError:
            print("Invalid date. Please try again.")