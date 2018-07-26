#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

def birthdays_list():
    birthdays = {
        "Шнибл: 23 марта": '-03-23',
        "Шана: 30 ноября": '-11-30',
        "Амадей: 17 января": '-01-17',
        "Фариах: 24 мая": '-05-24',
        "Алиса: 3 августа": '-08-03',
        "Василиса: 26 июля": '-07-26',
        "Федор: 20 июля": '-07-20',
        "Анна: 24 октября": '-10-24',
        "Света: 29 декабря": '-12-29',
        "Лена: 11 декабря": '-12-11'
    }

    birthdays_string = ""

    for key, value in birthdays:
        birthdays_string += key + " (" + get_wait_days(value) + " дней осталось)\n"

    # birthday_shnible = '-03-23'
    # birthday_shana = '-11-30'
    # birthday_amadey = '-01-17'
    # birthday_fariah = '-05-24'
    # birthday_alisa = '-08-03'
    # birthday_vasilisa = '-07-26'
    # birthday_fedor = '-07-20'
    # birthday_anna = '-10-24'
    # birthday_sveta = '-12-29'
    # birthday_lena = '-12-11'
    #
    #
    # amad_left = " (" + get_wait_days(birthday_amadey) + " дней осталось)\n"
    # shana_left = " (" + get_wait_days(birthday_shana) + " дней осталось)\n"
    # shnible_left = " (" + get_wait_days(birthday_shnible) + " дней осталось)\n"
    # fariah_left = " (" + get_wait_days(birthday_fariah) + " дней осталось)\n"
    # alisa_left = " (" + get_wait_days(birthday_alisa) + " дней осталось)\n"
    # vasilisa_left = " (" + get_wait_days(birthday_vasilisa) + " дней осталось)\n"
    # fedor_left = " (" + get_wait_days(birthday_fedor) + " дней осталось)\n"
    # anna_left = " (" + get_wait_days(birthday_anna) + " дней осталось)\n"
    # sveta_left = " (" + get_wait_days(birthday_sveta) + " дней осталось)\n"
    # lena_left = " (" + get_wait_days(birthday_lena) + " дней осталось)\n"
    #
    # amadey = "Амадей: 17 января" + amad_left
    # shana = "Шана: 30 ноября" + shana_left
    # shnible = "Шнибл: 23 марта" + shnible_left
    # fariah = "Фариах: 24 мая" + fariah_left
    # alisa = "Алиса: 3 августа" + alisa_left
    # vasilisa = "Василиса: 26 июля" + vasilisa_left
    # fedor = "Федор: 20 июля" + fedor_left
    # anna = "Анна: 24 октября" + anna_left
    # sveta = "Света: 29 декабря" + sveta_left
    # lena = "Лена: 11 декабря" + lena_left
    #
    # result = amadey + shana + shnible + fariah + alisa + vasilisa + fedor + anna + sveta + lena

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
