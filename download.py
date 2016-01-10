
import ssl
import pandas as pd
import urllib2
import time

def csv (url):
    context = ssl._create_unverified_context()
    retry_count = 5  # this is configured somewhere

    data = []

    for retries in range(retry_count):
        try:
            data = pd.read_csv(urllib2.urlopen(url, context=context))
            return data
        except Exception, e:
            print "retry " + retries
            time.sleep(4)

    return False

