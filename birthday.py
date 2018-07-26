#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


def birthdays_list():
    birthdays = {
        "Шнибл: 23 марта": get_wait_days('-03-23'),
        "Шана: 30 ноября": get_wait_days('-11-30'),
        "Амадей: 17 января": get_wait_days('-01-17'),
        "Фариах: 24 мая": get_wait_days('-05-24'),
        "Алиса: 3 августа": get_wait_days('-08-03'),
        "Василиса: 26 июля": get_wait_days('-07-26'),
        "Федор: 20 июля": get_wait_days('-07-20'),
        "Анна: 24 октября": get_wait_days('-10-24'),
        "Света: 29 декабря": get_wait_days('-12-29'),
        "Лена: 11 декабря": get_wait_days('-12-11')
    }

    sorted_birthdays_keys = sorted(birthdays, key=birthdays.get)

    sorted_birthdays = {}

    for key in sorted_birthdays_keys:
        sorted_birthdays[key] = birthdays[key]

    birthdays_string = ""

    for key, value in sorted_birthdays:
        if value == 0:
            birthdays_string += key + " (Ура, день рождения!)\n"
        else:
            birthdays_string += key + " (" + value + " дней осталось)\n"

    return birthdays_string


def get_wait_days(friend_birthday):
    current_year = str(datetime.date.today().year)
    birthday = current_year + friend_birthday
    a = birthday.split('-')
    aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
    bb = datetime.date.today()
    cc = aa - bb
    if(cc.days < 0):
        current_year = str(datetime.date.today().year + 1)
        birthday = current_year + friend_birthday
        birthday_a = birthday.split('-')
        birthday_aa = datetime.date(int(birthday_a[0]), int(birthday_a[1]), int(birthday_a[2]))
        bb = datetime.date.today()
        cc = birthday_aa - bb

    return str(cc.days)
