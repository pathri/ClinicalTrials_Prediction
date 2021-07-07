import pandas as pd
import numpy as np
# reading csv files
df1 = pd.read_csv('E:/Databases/conditions_03_2021.csv', na_values=[""], encoding='latin-1')
df2 = pd.read_csv('E:/Databases/interventions_03_2021.csv', na_values=[""])
df3 = pd.read_csv('E:/Databases/studies_03_2021.csv', na_values=[""])
mid= pd.merge(df1, df2, how='outer', on='nct_id')
output= pd.merge(mid, df3, how='outer', on='nct_id')
# displaying result
print(output)
output.to_csv('E:/Databases/final_03_2021_outer.csv', index=False)