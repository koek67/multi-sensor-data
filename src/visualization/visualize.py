import pandas as pd
import os.path

local = True

data_set_url = '/nethome/kkrishnan8/multi-sensor-data/data/raw/PEACHData/'
if local:
    data_set_url = '/Users/koushikkrishnan/Documents/CODE/multi-sensor-data/data/raw/PEACHData/'

user_profiles = pd.read_csv(os.path.join(data_set_url, 'User Profiles/up_explicit_data.csv'))
body_temp = pd.read_csv(os.path.join(data_set_url, 'IoT/iot_bodytemp_data.csv'), parse_dates=['DateTime'])
heart_rate = pd.read_csv(os.path.join(data_set_url, 'IoT/iot_heartrate_data.csv'), parse_dates=['DateTime'])
sleep_quality = pd.read_csv(os.path.join(data_set_url, 'IoT/iot_sleepquality_data.csv'), parse_dates=['DateTime'])

avg_body_temp_by_user = body_temp.groupby(['UserId']).mean()

increased_heart_rate = heart_rate[['UserId', 'Increased_Heart_Rate']]
resting_heart_rate = heart_rate[['UserId', 'User_Resting_Heart_Rate']]
avg_increased_heart_rate = increased_heart_rate.groupby(['UserId']).mean()
avg_resting_heart_rate = resting_heart_rate.groupby(['UserId']).mean()

avg_body_temp_by_user.plot()