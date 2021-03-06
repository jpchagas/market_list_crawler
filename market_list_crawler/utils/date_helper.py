from datetime import date, datetime, timedelta
import calendar

today = date.today()


def current_date():
    return today.strftime("%d-%m-%Y")


def string_date(str_date):
    return datetime.strptime(str_date, '%d-%m-%Y').date()


def get_weekday_name(day):
    return calendar.day_name[day.weekday()]


def get_dates():
    days_list = []
    begin_date = date(2019, 11, 28)
    end_date = date(2020, 11, 21)

    delta = end_date - begin_date

    for i in range(delta.days + 1):
        day = begin_date + timedelta(days=i)
        #if get_weekday_name(day) == 'Tuesday' or get_weekday_name(day) == 'Thursday':
        days_list.append(day)
    return days_list