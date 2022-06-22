from pathlib import Path
import pandas as pd

# import the raw data into a dataframe
df = pd.read_csv(Path('data/raw/Fire_Open_Data.csv'), dtype=str)

# convert column data types as needed
df['ZIP_CODE'] = df['ZIP_CODE'].astype(str).str.zfill(5)
df['PRIORITY'] = df['PRIORITY'].astype(int)
df['DATE'] = pd.to_datetime(df['DATE'])
df['CREATE'] = pd.to_datetime(df['CREATE'])
df['CLEAR'] = pd.to_datetime(df['CLEAR'])

# rename columns for consistency
df = df.rename(columns={'EVENT TYPE':'EVENT_TYPE', 
                    'HOUR OF':'HOUR_OF', 
                    'FD EVENT NUMBER':'FD_EVENT_NUMBER'})

# add the event category field
category = df['EVENT_TYPE'].str.split('--', n=1, expand=True)
df['EVENT_CATEGORY'] = category[0]

# add the time to clear field
df['TIME_TO_CLEAR'] = ((df['CLEAR'] - df['CREATE']).astype('timedelta64[m]') + 
                    ((df['CLEAR'] - df['CREATE']).astype('timedelta64[h]') * 60))
df['TIME_TO_CLEAR'] = df['TIME_TO_CLEAR'].astype(int)

# write the clean data files
df.to_csv(Path('data/clean/fire_dashboard.csv'), index=False)
df.to_json(Path('data/clean/fire_dashboard.json'), orient='records')
