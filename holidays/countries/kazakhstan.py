# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2020
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date

from holidays.constants import JAN, MAR, MAY, JUN, JUL, AUG, DEC
from holidays.holiday_base import HolidayBase
from holidays.utils import get_gre_date


class Kazakhstan(HolidayBase):
    """
    This class doesn't return any holidays before 1991-01-01.
    https://egov.kz/cms/en/articles/holidays-calend
    """

    def __init__(self, **kwargs):
        self.country = "KZ"
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        if year < 1991:
            return

        # New Year's Day
        name = "Новый год"
        self[date(year, JAN, 1)] = name
        self[date(year, JAN, 2)] = name

        # Christmas Day (Orthodox)
        if year > 2005:
            self[date(year, JAN, 7)] = "Рождество Христово " \
                                   "(православное Рождество)"

        # International Women's Day
        self[date(year, MAR, 8)] = "Международный женский день"

        # Nauryz holiday
        name = "Наурыз мейрамы"
        self[date(year, MAR, 22)] = name
        if year > 2008:
            self[date(year, MAR, 21)] = name
            self[date(year, MAR, 23)] = name

        # Kazakhstan's People Solidarity Holiday
        if year > 1995:
            name = "Праздник единства народа Казахстана"
        else:
            name = "День международной солидарности трудящихся"
        self[date(year, MAY, 1)] = name

        # Defenders’ day
        if year > 2012:
            self[date(year, MAY, 7)] = "День защитника Отечества"

        # Victory Day
        self[date(year, MAY, 9)] = "День Победы"

        # Capital Day
        if year > 2008:
            self[date(year, JUL, 6)] = "День Столицы"

        # First day of Qurban Ait - (hijari_year, 12, 10)
        if year >= 2006:
            for date_obs in get_gre_date(year, 12, 10):
            hol_date = date_obs
            self[hol_date] = "Курбан-айт"

        # Constitution Day of the Kazakhstan
        if year > 1994:
            self[date(year, AUG, 30)] = "День Конституции РК"

        # First President Day
        if year > 2011:
            self[date(year, DEC, 1)] = "День Первого Президента РК"

        # Kazakhstan Independence Day
        name = "День Независимости"
        self[date(year, DEC, 16)] = name
        self[date(year, DEC, 17)] = name


class KZ(Kazakhstan):
    pass


class KAZ(Kazakhstan):
    pass
