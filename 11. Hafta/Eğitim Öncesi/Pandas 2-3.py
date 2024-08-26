import pandas as pd
import numpy as np

m = np.arange(1,10).reshape((3,3))
df = pd.DataFrame(m, columns=['var1','var2','var3'])
a = df.head(2)
print(a)