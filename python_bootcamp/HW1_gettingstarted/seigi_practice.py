import pandas as pd
import os
import numpy as np

os.chdir('C:/Users/seigi/Documents/GSI/ERG-190C-Staff/homework/HW1 getting started')

data3 = pd.read_csv("data/q2_3.csv").as_matrix()

print(np.sum(data3[:,2:9]))
