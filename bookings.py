from QuantLib import *
from functools import *
from itertools import *
import pandas as pd
import sympy as sp
import json

Obs = {
    "USDLibor6M": 0.0097,
    "USDLibor3M": 0.0077,
}

Contract = {
    'calendar':         'Hong Kong stock exchange',
    'leg1':             'coupon1 * cov',
    'leg2':             'coupon2 * cov',
    'counterparty':     'Potomac',
    'coupon1':          0.039,
    'coupon2':          'index1 * 1 + spread1',
    'cov':              1.011,
    'date_adjust':      1,
    'daycount1':        'Actual/360',
    'daycount2':        'Actual/360',
    'end_end':          '2017-12-31',
    'id':               1,
    'notional':         10_000_000,
    'index1':           'USDLibor6M',
    'schedule1':        ['2017-01-01', '2017-12-31'],
    'schedule2':        ['2017-01-01', '2017-12-31'],
    'spread1':          0.022,
    'start_date':       '2017-01-01',
    "delivery":         'cash',
}

def public_holidays(c, start, num_days=365):
    for i in range(0,num_days):
        raw_date = start + Period(i, Days)
        if not c.isBusinessDay(raw_date) and not c.isWeekend(raw_date.weekday()):
            print(raw_date)


def rec_eval(s, m):
    ex = sp.simplify(s)
    ex_next = ex.subs(m)
    if ex == ex_next:
        if type(ex.evalf()) == sp.Float:
            return ex
        else:
            raise Exception("non-exhaustive eval " + str(ex))
    else:
        return rec_eval(ex_next, m)


if __name__ == '__main__':
    public_holidays(HongKong(), Date(1,1,2017))


