from datetime import datetime

def get_days_from_today(date):
    input_date = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.today()
    difference = current_date - input_date
    return difference.days
