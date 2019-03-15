
import json
from pprint import pprint

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[str(name[:-1])] = str(x)

    flatten(y)
    return out


# not tested with lists
def flatten_json_only_leafs(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a)
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i))
                i += 1
        else:
            out[str(name[:-1])] = str(x)

    flatten(y)
    return out


## example
with open('data.json') as data_file:    
    data = json.load(data_file)

pprint(flatten_json_only_leafs(data))



## see also the pandas approach
# https://medium.com/@amirziai/flattening-json-objects-in-python-f5343c794b10#.jl3dtxky5
from pandas.io.json import json_normalize
print json_normalize(data).columns.values