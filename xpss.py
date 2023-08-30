#!/usr/bin/env python
# coding: utf-8

#pip install pandas


#Xplane scenery sorter
import pandas as pd


# In[138]:

filename='scenery_packs.ini'

outfilename=False

import sys
if len(sys.argv)>1: filename=sys.argv[1]
if len(sys.argv)>2: outfilename=sys.argv[2]

sys.stderr.write("xpss\n")
sys.stderr.write("processing "+filename+"\n\n")

with open(filename) as f:
    lines = f.readlines()
    
sceneries = list(map(lambda x:x.strip(),list(filter(lambda x:x.startswith("SCENERY_PACK"), lines))))
header = list(map(lambda x:x.strip(),lines[0:4])) #first 4 lines -- obviously dirty :)


# In[170]:


## Load Config File
with open('config.txt') as f:
    lines = f.readlines()
    
config = map(lambda x: {
    "cat": int(x.split()[0]),
    "val": x.split()[1:][0]
    }, 
    map(lambda x: x.strip(), 
      filter(lambda x: not x.startswith("#") and len(x)>1, lines)))

config = list(config)


# In[132]:


# Sort the scenery

def findcat(txt, conf):
    for x in conf:
        if txt.find(x['val'])>=0: return x['cat']
    return #f




# In[160]:


folders = list(map(lambda x: " ".join(x.split()[1:]), sceneries))


# In[171]:


data = pd.DataFrame(data=list(map(lambda x: [findcat(x, config), x], folders)),
             columns=['order', 'folder'])


# In[179]:


result = data.sort_values(by=['order', 'folder']).drop_duplicates(subset='folder').values


# In[184]:


scen_disabled = list(map(lambda x: x[1], list(filter(lambda x: x[0]<0, result))))
scen_enabled = list(map(lambda x: x[1], list(filter(lambda x: x[0]>=0, result))))


# In[192]:


inistr = list(map(lambda x: "SCENERY_PACK_DISABLED "+x, scen_disabled)) + list(map(lambda x: "SCENERY_PACK "+x, scen_enabled))
if outfilename:
    print("Writing to "+outfilename)
    of = open(outfilename, "w")
    of.write('\n'.join(header+inistr))
    of.write('\n')
    of.close()
else:
    sys.stderr.write("writing to stdout as no outfile was given\n\n\n")
    print('\n'.join(header+inistr))
