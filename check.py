import os
import re
path = os.listdir("/Users/zhangyunping/Desktop/assignment1")
# pattern  = re.compile(r'\d+')
names = []
path.remove('.DS_Store')
path.remove('submitted.csv')
for p in path:
    # num = re.findall(pattern,p)
    names.append(p.split('_')[0])


import pandas as pd

enrolled = pd.read_csv("/Users/zhangyunping/Desktop/group_arrangement_v1.0.csv")
std_names = enrolled['Name'].values
N = []
error =[]
miss = 'Miss '
mr = 'Mr. '
ms = 'Ms. '
for name in std_names:
    if name.startswith(miss):
        N.append(name[len(miss):])
    elif name.startswith(mr):
        N.append(name[len(mr):])
    elif name.startswith(ms):
        N.append(name[len(mr):])
    else:
        error.append(name)


for name in N:
    if name in names:
        continue
    else:
        print(name)