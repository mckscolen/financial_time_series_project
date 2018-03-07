#Import all required libraries
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import scipy
import pandas_datareader as pdr
import datetime
from sklearn import preprocessing

class FinancialTimeSeries():
    
    def __init__(self, name, data, data_field, time_field='Date'):
        self.name = name
        
        if not isinstance(data.index, pd.core.indexes.datetimes.DatetimeIndex):
            data[time_field] = pd.to_datetime(data[time_field])
            data.set_index(time_field)
            
        self.data = data[data_field]
        self.data_field = data_field
        
        #build the normalized data seres
        self.data_field_scaled = 'n{0}'.format(data_field)
        data[self.data_field_scaled] = preprocessing.scale(data[data_field])
        #data[self.data_field_scaled] = preprocessing.normalize(data[data_field], norm='l2')
        self.data_scaled = data[self.data_field_scaled]
        
    def variance(self, days):
        return(self.data.rolling(window=days,center=True).var())
    
    def variance_scaled(self,days):
        return(self.data_scaled.rolling(window=days,center=True).var())
    
    def standard_deviation(self, days):
        return(self.data.rolling(window=days,center=True).std())
    
    def standard_deviation_scaled(self,days):
        return(self.data_scaled.rolling(window=days,center=True).std())
    
    def trend(self,days):
        return(self.data.rolling(window=days,center=True).mean())
    
    def trend_scaled(self,days):
        return(self.data_scaled.rolling(window=days,center=True).mean())
        
    def histogram(self):
        self.data.hist()
        plt.xlabel('Time')
        plt.ylabel(self.data_field)
        plt.title('Histogram')
        plt.show()
    
    def histogram_scaled(self):
        self.data_scaled.hist()
        plt.xlabel('Time')
        plt.ylabel(self.data_field_scaled)
        plt.title('Scaled Histogram')
        plt.show()
  
    
class FinancialTimeSeriesPlots():
    
    def __init__(self):
        
        #this allows user to easily switch between normalized and non-normalized series
        self.time_series = {}
        self.is_scaled = False
        
        #set up universal plot properties
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.title('Time Series')      
        
        self.properties = {
            'Series'   : (lambda ts, days: plt.plot(ts.data,label = ts.data_field)),
            'Trend'    : (lambda ts, days: plt.plot(ts.trend(days),label = ts.data_field)),
            'Variance' : (lambda ts, days: plt.plot(ts.variance(days),label = ts.data_field)),
            'Std'      : (lambda ts, days: plt.plot(ts.standard_deviation(days),label = ts.data_field))
        }
        
        self.properties_scaled = {
            'Series'   : (lambda ts, days: plt.plot(ts.data_scaled,label = ts.data_field_scaled)),
            'Trend'    : (lambda ts, days: plt.plot(ts.trend_scaled(days),label = ts.data_field_scaled)),
            'Variance' : (lambda ts, days: plt.plot(ts.variance_scaled(days),label = ts.data_field_scaled)),
            'Std'      : (lambda ts, days: plt.plot(ts.standard_deviation(days),label = ts.data_field_scaled))           
        }
        
    def using_scaled(self):
        return(self.is_normal)
    
    def switch_scaled(self):
        self.is_scaled = not self.is_scaled
        
    def add_time_series(self,series):
        self.time_series[series.name] = series
        
    def remove_time_series(self,name):
        self.time_series.remove(name)
        
    def get_time_series(self, name):
        return(self.time_series[name])
    
    def plot_time_series(self,series_property, days=15, name=None):
        
        if name is None:
            for n,ts in self.time_series.items():
                if self.is_scaled:
                    self.properties_scaled[series_property](self.time_series[n], days)
                else:
                    self.properties[series_property](self.time_series[n], days)               
        else:        
            if self.is_scaled:
                self.properties_scaled[series_property](self.time_series[name], days)
            else:
                self.properties[series_property](self.time_series[name], days)
        
        plt.legend(loc='best')
        return(plt)
    
    
        