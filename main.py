#%%
#%%

import os
import sys

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
sys.path.append('/')

from pack.SAP_join_data import JoinSapData

join_data = JoinSapData()


