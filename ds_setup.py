
#import sys; import os; sys.path.append(os.path.expanduser('~/DropBox/my/projects/python/'))
import sys; import os; sys.path.append(os.path.expanduser('~/Google Drive/my/projects/T/'))

import matplotlib
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

import pandas   as pd
import operator as op

import numpy             as np
import seaborn           as sns
from datetime import datetime

import pyscope
from pyscope import read_ss

from T import * # want T to be super accessible
#import stats as stats
from datascience import *

import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


#import altair as alt
#from vega_datasets import data
#alt.data_transformers.enable('json')
def set_plt_format():
#    sns.set() # seaborn coloring
    sns.set(font='Segoe UI', rc={'figure.figsize':(11.7,6.27), 'font.size':11 \
                                ,'axes.titlesize':18,'axes.labelsize':13 \
                                ,'axes.titlepad' : 20,'axes.labelpad': 10 })
    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.1)
    #plt.subplots_adjust(top=0.1)

# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all" # Interactive matplot lib charts
