#!/usr/bin/env python
# coding: utf-8

# In[2]:


#pip install pandas


# In[3]:


#Xplane scenery sorter
import pandas as pd


# In[138]:


with open('scenery_packs.ini') as f:
    lines = f.readlines()
    
sceneries = list(map(lambda x:x.strip(),list(filter(lambda x:x.startswith("SCENERY_PACK"), lines))))


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


inistr = list(map(lambda x: "SCENERY_DISABLED "+x, scen_disabled)) + list(map(lambda x: "SCENERY "+x, scen_enabled))
print('\n'.join(inistr))

