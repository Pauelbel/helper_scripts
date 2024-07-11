# https://www.codewars.com/kata/563c13853b07a8f17c000022/train/python

from datetime import datetime


def is_today(date):
    current_day = datetime.now()
    return (
        date.year == current_day.year
        and date.month == current_day.month
        and date.day == current_day.day
    )


def is_today_best(date):
    return date.date() == datetime.today().date()
