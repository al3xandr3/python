

import sys; import os; sys.path.append(os.path.expanduser('~/DropBox/my/projects/python/'))
import pandas as pd
import stats as stats
import datetime as datetime
import datedimension as dim
import numberformatter as form
import download as download
import matplotlib.pyplot as mat
import wcloud as wcloud

import seaborn as sns
sns.set_style("whitegrid")

# clipboard -> data frame
data = pd.read_clipboard()

data
data.describe()


# HISTOGRAM
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html
plt = data.hist()
plt = data.hist(bins=100)


# BOX PLOT
plt = sns.boxplot(x="type", y="value", data=data[-100:])
plt.set(title="My Box plot")


# WORD CLOUD
wcloud.cloudy(' '.join(data['type'].values))


# 95% confidence interval
stats.confidence_interval(data['value'].values, confidence=0.95)