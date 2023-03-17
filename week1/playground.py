#%% install numpy
!pip install numpy

#%% Imports
import numpy as np

#%% Index an array

array = np.array([0, 1,2,3,4,5, 6])
array[[1,2,5]]

#%% install pandas
!pip install pandas

#%% import pandas
import pandas as pd

#%% Test
index = ['Apple', 'Banana', 'Orange']
quantity = [34, 20, 30, 40]
pd.Series(data = quantity, index = index)

#%% Multiple Masks
array = np.arange(25).reshape((5,5))

array[[array // 2 == 0, array > 3], 2:3]

#%% install matplotlib and seaborn
!pip install matplotlib
!pip install seaborn

#%% import 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns