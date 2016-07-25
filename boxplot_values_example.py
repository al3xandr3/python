
import sys; import os; sys.path.append(os.path.expanduser('~/DropBox/my/projects/python/'))
import stats
import pandas 

import matplotlib.pyplot as plt

data = pandas.read_csv('surv2.txt', sep=',')

print stats.boxplot_values (data)
