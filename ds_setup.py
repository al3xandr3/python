
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

import t as t


import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)
