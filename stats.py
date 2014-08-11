
import statsmodels.api as sm
import pandas as pd

def relative_change(new, reference):
    return ((float(new) - float(reference)) / float(reference)) * 100

# linear regression fit
def linear_fit (data_ar):
    ndt = data_ar
    X = pd.Series(range(1, len(ndt) + 1))
    y = ndt
    # ordinary least squares 
    fit = sm.OLS(y,sm.add_constant(X)).fit().fittedvalues
    return fit.values
# linear_fit (['1,2,3,4,5'])

# moving average fit
def mov_avg_fit (data_ar, period):
    X = data_ar
    return pd.rolling_mean(X, period)
# mov_avg_fit (['1,2,3,4,5'], 2)
