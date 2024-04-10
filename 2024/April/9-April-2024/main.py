import pandas as pd

df =  pd.read_json('/workspaces/Random-Python-Work/2024/April/9-April-2024/MDIA.json',lines=True)    
print(df.columns)