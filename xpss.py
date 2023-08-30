#!/usr/bin/env python
# coding: utf-8

#pip install pandas


#Xplane scenery sorter
import pandas as pd

import argparse
parser = argparse.ArgumentParser(
                    prog='xpss',
                    description='X-Plane Scenery Sorter',
                    epilog='(C)2023 bonk')

parser.add_argument('-i', '--ini', help='read scenery_pack.ini input file, default: scenery_packs.ini', default='scenery_packs.ini')
parser.add_argument('-s', '--scandir', help='dont read ini file but scan Custom Scenery directory', default=False)
parser.add_argument('-c', '--config', help='specify config file, default: config.txt', default='config.txt')
parser.add_argument('-o','--out', help='write output to file', default=False)
#parser.add_argument('--dry', help='dryrun')
parser.add_argument('-d','--debug', help='debug', action='store_true')
args = parser.parse_args()

print(args)

filename=args.ini



import sys

sys.stderr.write("xpss\n")

if not args.scandir:
    sys.stderr.write("processing "+filename+"\n\n")
    with open(filename) as f:
        lines = f.readlines()
    
    sceneries = list(map(lambda x:x.strip(),list(filter(lambda x:x.startswith("SCENERY_PACK"), lines))))
    header = list(map(lambda x:x.strip(),lines[0:4])) #first 4 lines -- obviously dirty :)

if args.scandir:
    import os
    dirs = os.listdir(args.scandir)
    sceneries = list(map(lambda x: "Custom Scenery/"+x+"/", filter(lambda x: os.path.isdir(x) and not x.startswith("."), dirs)))
    sceneries += ['*GLOBAL_AIRPORTS*']
    folders = sceneries
    header = ["I","1000 Version","SCENERY", ""]




if args.debug: sys.stderr.write(",".join(sceneries)+"\n" )


# In[170]:


## Load Config File
with open(args.config) as f:
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


folders = folders or list(map(lambda x: " ".join(x.split()[1:]), sceneries))


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
if args.out:
    print("Writing to "+args.out)
    of = open(args.out, "w")
    of.write('\n'.join(header+inistr))
    of.write('\n')
    of.close()
else:
    sys.stderr.write("writing to stdout as no outfile was given\n\n\n")
    print('\n'.join(header+inistr))
