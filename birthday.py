#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

def birthdays_list():
    birthday_shnible = '-03-23'
    birthday_shana = '-11-30'
    birthday_amadey = '-01-17'
    birthday_fariah = '-05-24'

    amad_left = " (" + get_wait_days(birthday_amadey) + " дней осталось)\n"
    shana_left = " (" + get_wait_days(birthday_shana) + " дней осталось)\n"
    shnible_left = " (" + get_wait_days(birthday_shnible) + " дней осталось)\n"
    fariah_left = " (" + get_wait_days(birthday_fariah) + " дней осталось)\n"

    amadey = "Амадей: 17 января" + amad_left
    shana = "Шана: 30 ноября" + shana_left
    shnible = "Шнибл: 23 марта" + shnible_left
    fariah = "Фариах: 24 мая" + fariah_left

    result = amadey + shana + shnible + fariah

    return result


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
