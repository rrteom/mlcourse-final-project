import numpy as np
import pandas as pd

import requests
import sys
import os

activity_dict = {
    1: 'inactive',
    2: 'inactive',
    3: 'inactive',
    4: 'walking',
    5: 'running',
    6: 'cycling',
    16: 'household_activities',
    17: 'household_activities'
}

url = sys.argv[1]

dir_path = os.path.abspath(os.path.dirname(__file__))

df_init = pd.read_csv(os.path.join(dir_path, 'smallest_sample_for.test'))

row_number = int(sys.argv[2]) % len(df_init) if len(sys.argv) >= 3 else np.random.randint(len(df_init))


df_test = pd.DataFrame(df_init.iloc[row_number]).T.drop(columns=['subjectID', 'activityID'])
true_label = df_init.iloc[row_number]['activityID']

data = dict(df_test.iloc[0])

if __name__ == '__main__':
    print(f'row number: {row_number}')
    response = requests.post(url, json=data).json()
    print(response)
    print(f'true_label: {activity_dict[true_label]}')