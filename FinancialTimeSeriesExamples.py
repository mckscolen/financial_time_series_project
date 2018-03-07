#Import all required libraries
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import scipy
import pandas_datareader as pdr
import datetime
from sklearn import preprocessing
from FinancialTimeSeriesPackage import *

#download market data
DJIA = pdr.fred.FredReader('DJIA').read().dropna()
NASDAQCOM = pdr.fred.FredReader('NASDAQCOM').read().dropna()
SP500 = pdr.fred.FredReader('SP500').read().dropna()
DEXUSEU = pdr.fred.FredReader('DEXUSEU').read().dropna()
DEXUSUK = pdr.fred.FredReader('DEXUSUK').read().dropna()

dow_jones = FinancialTimeSeries('Dow Jones Industrial', DJIA, 'DJIA')
nasdaq    = FinancialTimeSeries('NASDAQ', NASDAQCOM, 'NASDAQCOM')
sp500     = FinancialTimeSeries('SP 500', SP500, 'SP500')
usd_eur   = FinancialTimeSeries('USD to EUR', DEXUSEU, 'DEXUSEU')
us_gbp    = FinancialTimeSeries('USD to GBP', DEXUSUK, 'DEXUSUK')

plots = FinancialTimeSeriesPlots()
plots.add_time_series(dow_jones)
plots.add_time_series(nasdaq)
plots.add_time_series(sp500)
plots.add_time_series(usd_eur)

plots.plot_time_series('Series', 60, dow_jones.name).show()
dow_jones.histogram()

plots.plot_time_series('Series', 60, nasdaq.name).show()
nasdaq.histogram()