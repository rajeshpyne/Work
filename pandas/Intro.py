import pandas as pd
import numpy as np

#Series

s = pd.Series([1,'a',2.4,{'z':1,"x":3}],index=["a","b","c","d"])
r = pd.Series([1,'a',2.4,{'z':1,"x":3}])
print(s)
print(r)