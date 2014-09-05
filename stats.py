
import pandas as pd

def relative_change(new, reference):
    return ((float(new) - float(reference)) / float(reference)) * 100

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

def confidence_interval (s):
    from scipy import stats
    import scipy as sp
    import numpy as np
    import math
    n, min_max, mean, var, skew, kurt = stats.describe(np.array(s))
    std=math.sqrt(var)
    
    #The location (loc) keyword specifies the mean.
    #The scale (scale) keyword specifies the standard deviation.
    # We will assume a normal distribution
    R = stats.norm.interval(0.975,loc=mean,scale=std/math.sqrt(len(s)))
    return R
#confidence_interval([1,2,3,4,4,4,5,5,5,5,4,4,4,6,7,8])
