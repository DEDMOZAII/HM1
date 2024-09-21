from datetime import datetime

def get_days_from_today(date):
    try:
        date_str = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        difference_date = current_date - date_str
        return difference_date.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."
print(get_days_from_today("2020-10-13"), "days")