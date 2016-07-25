
import pandas as pd


def relative_change(new, reference):
    return ((float(new) - float(reference)) / float(reference)) * 100


def confidence_interval(data, confidence=0.95):
    import numpy as np
    import scipy as sp
    import scipy.stats

    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
    return m, m-h, m+h
#confidence_interval([1,2,3,4,4,4,5,5,5,5,4,4,4,6,7,8])

def linear_fit (data_ar):
    import statsmodels.api as sm
    import pandas as pd
    ndt = data_ar
    X = pd.Series(range(1, len(ndt) + 1))
    y = ndt
    # ordinary least squares 
    fit = sm.OLS(y,sm.add_constant(X)).fit()
    return {'params': fit.params.values, 'fit_values': fit.fittedvalues.values}
# linear_fit ([1,2,2,4,4,5])['params']
# linear_fit ([1,2,2,4,4,5])['fit_values']


# moving average fit
def mov_avg_fit (data_ar, period):
    X = data_ar
    return pd.rolling_mean(X, period)
# mov_avg_fit (['1,2,3,4,5'], 2)

# moving average fit
def boxplot_values (data_df):
    x =  data_df
    return [
         x.min().values[0]
         ,x.quantile(.25).values[0]
        ,x.median().values[0]
        ,x.quantile(.75).values[0]
        ,x.max().values[0]
        ]

#print boxplot_values([377,571,248,573,341,314,1007,398,158,192,405,404,286,176,167,900])
