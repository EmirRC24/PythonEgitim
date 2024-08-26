import numpy as np
import pandas as pd

m = np.arange(1, 10).reshape((3, 3))
df = pd.DataFrame(m, columns=["1", "2", "3"])
print(df)