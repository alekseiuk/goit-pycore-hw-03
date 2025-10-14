from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Time data does not match format"
    except TypeError:
        return "Argument must be string"
    else:
        current_date = datetime.today()
        difference = current_date - input_date
        return difference.days
