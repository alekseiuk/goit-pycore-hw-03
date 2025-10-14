from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_birthday = user_birthday.replace(year=today.year)
    
        if user_birthday < today:
            user_birthday = user_birthday.replace(year=today.year + 1)

        time_to_birthday = (user_birthday - today).days
        
        if 0 <= time_to_birthday <= 7:
            congratulation_date = user_birthday

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays
