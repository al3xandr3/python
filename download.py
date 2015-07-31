
import ssl
import pandas as pd
import urllib2

def csv (url):
    context = ssl._create_unverified_context()
    return pd.read_csv(urllib2.urlopen(url, context=context))
