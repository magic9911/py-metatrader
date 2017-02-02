'''
Created on 2015/04/15

@author: Taiga
'''

from nose.core import run
from metatrader.mt4 import initizalize
from metatrader.backtest import BackTest
from datetime import datetime
import logging

def test_backtest():
    logging.basicConfig(level=logging.DEBUG)
    initizalize('C:\\Program Files (x86)\\MetaTrader 4')

    from_date = datetime(2016, 5, 1)
    to_date = datetime(2017, 1, 1)

    ea_name = 'Moving Average'
    param = {
             'Lots': {'value': 0.1},
             'MaximumRisk': {'value': 0.02, 'max': 0.2, 'interval': 0.05},
             'DecreaseFactor': {'value': 3.0},
             'MovingPeriod': {'value': 12},
             'MovingShift': {'value': 6}
             }


    backtest = BackTest(ea_name, param, 'EURUSD', 'M5', from_date, to_date, spread=10)

    ret = backtest.run()
    a=0


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    import os
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    test_backtest()
