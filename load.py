import json
import numpy as np
import pandas as pd

from dd import down, down2
from dddd import Downloader

rc = pd.read_csv('./bb',names=['title'])
rc.set_index('title')


rc2 = pd.read_csv('./newdownlist.csv', names=['title', 'url'])
rc2.set_index('title')

d = dict(zip(rc2['title'],rc2['url']))
# print(d)

# print(rc2.columns[0])
# print(rc2.loc[1])

# rc2.to_dict(rc2.loc['title'],rc2.loc['url'])
# print(rc2)

# d = pd.concat([rc2,rc],join='inner')
# print(d)
i = 0
for t in rc['title']:

    print(i,d[t])
    i+=1
    # down(d[t],f"xxx/{t}.rar",0)
    downloader = Downloader(d[t],f"xxx/{t}.rar")
    downloader.start()