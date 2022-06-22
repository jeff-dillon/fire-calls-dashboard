import os
from pathlib import Path
import pandas as pd
import numpy as np

# import the raw data into a dataframe
df = pd.read_csv(Path('data/raw/Fire_Open_Data.csv'), dtype=str)

# convert column data types as needed
df['ZIP_CODE'] = df['ZIP_CODE'].astype(str).str.zfill(5)
df['PRIORITY'] = df['PRIORITY'].astype(int)
df['CREATE_DT'] = pd.to_datetime(df['DATE'] + df['CREATE'], format='%m/%d/%Y%H:%M:%S')
df['CLEAR_DT'] = pd.to_datetime(df['DATE'] + df['CLEAR'], format='%m/%d/%Y%H:%M:%S')

# rename columns for consistency
df = df.rename(columns={'EVENT TYPE':'EVENT_TYPE', 
                    'HOUR OF':'HOUR_OF', 
                    'FD EVENT NUMBER':'FD_EVENT_NUMBER'})

# add the event category field
category = df['EVENT_TYPE'].str.split('--', n=1, expand=True)
df['EVENT_CATEGORY'] = category[0]

# add the time to clear field
# this represents the number of minutes that elapse from when the call is created to when it is cleared
# special care has to be taken for calls that span over the course of more than one day
df['CLEAR_DT'] = np.where(df['CLEAR_DT'] < df['CREATE_DT'], df['CLEAR_DT'] + pd.DateOffset(days=1),df['CLEAR_DT'])
df['TIME_TO_CLEAR'] = ((df['CLEAR_DT'] - df['CREATE_DT']).astype('timedelta64[m]'))
df['TIME_TO_CLEAR'] = df['TIME_TO_CLEAR'].astype(int)

# make sure the clean data folder exists
clean_data_folder = ('data/clean')
check_folder = os.path.isdir(clean_data_folder)
if not check_folder:
    os.makedirs(clean_data_folder)

# write the clean data files
df.to_csv(Path('data/clean/fire_dashboard.csv'), index=False)
