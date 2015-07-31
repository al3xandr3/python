
# Install lib: http://stickpeople.com/projects/python/win-psycopg/

import psycopg2

def connect(host, dbname, user, port, password):
    conn_str = "host='%s' port='%s' dbname='%s' user='%s' password='%s'" % (host, port, dbname, user, password)
    try:
        conn = psycopg2.connect(conn_str)
    except:
    	print "problem connecting to database\n"
    return conn
