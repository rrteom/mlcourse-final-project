# mlcourse-final-project

## Project description
The project is a containerized flask app for classification of physical activities from the list:
1. inactive
2. walking
3. running
4. cycling
5. household_activities

## Model info
The model consists of following steps:
1. KMeans clustering 
2. Classifier (lightgbm gbdt multiclass classifier) on input data and cluster labels form KMeans


The model was trained on 4 and tested on other 3 subjects from PAMAP2 dataset, for futher info on model training and metrics see notebooks/classification_w_clusters.ipynb.


## Dataset info
Physical Activity Monitoring dataset<br>
https://archive.ics.uci.edu/dataset/231/pamap2+physical+activity+monitoring<br>
more detainls in dataset_readme.pdf<br>
Link to merged and downsampled datasets (out csv files from data_preparation/data_prep.ipynb and data_preparation/data_prep0.ipynb):
```
https://drive.google.com/drive/folders/14WBNoNCtKN6On09xhDHzK_3nUOmR9V-V?usp=sharing
```

## API description
POST /
```
{
    "feature_name": value,
    ...
}
```
feature_names list: 
```
['heart rate',
 'hand_temperature',
 'hand_acceleration16_x',
 'hand_acceleration16_y',
 'hand_acceleration16_z',
 'hand_acceleration6_x',
 'hand_acceleration6_y',
 'hand_acceleration6_z',
 'hand_gyroscope_x',
 'hand_gyroscope_y',
 'hand_gyroscope_z',
 'hand_magnetometer_x',
 'hand_magnetometer_y',
 'hand_magnetometer_z',
 'chest_temperature',
 'chest_acceleration16_x',
 'chest_acceleration16_y',
 'chest_acceleration16_z',
 'chest_acceleration6_x',
 'chest_acceleration6_y',
 'chest_acceleration6_z',
 'chest_gyroscope_x',
 'chest_gyroscope_y',
 'chest_gyroscope_z',
 'chest_magnetometer_x',
 'chest_magnetometer_y',
 'chest_magnetometer_z',
 'ankle_temperature',
 'ankle_acceleration16_x',
 'ankle_acceleration16_y',
 'ankle_acceleration16_z',
 'ankle_acceleration6_x',
 'ankle_acceleration6_y',
 'ankle_acceleration6_z',
 'ankle_gyroscope_x',
 'ankle_gyroscope_y',
 'ankle_gyroscope_z',
 'ankle_magnetometer_x',
 'ankle_magnetometer_y',
 'ankle_magnetometer_z']
 ```
 example response (probabilities):
 ```
 {
    'cycling': 0.5268814269287857,
    'household_activities': 0.011617551694845251,
    'inactive': 0.018165760683611913,
    'running': 0.42336618857141467,
    'walking': 0.019969072121342454
}
```

## How to run the app
Create docker image:
From mlcourse-final-project directory run the following command
```
docker duild -t pamap_app .
```
Run container:
```
docker run --rm -dp 5678:5678 --name pamap-app-container pamap_app:latest
```

Stop and delete the container:
```
docker stop pamap-app-container
```

## How to use example_client
```
python path/to/example_client/example_client.py <http-address> [row_number]
```
in current configuration the app listens to port 5678<br>
if client launched on app host http-address=`http://127.0.0.1:5678/`

row_number: any nonnegative integer to take row_number'th row from `smallest_sample_for.test`<br>
if not specified row_number is chosen randomly, if exceeds test data length row_number = row_number % data_len<br>
The client chooses random (if not specified otherwise) row from smallest_sample_for.test, converts it into API-compatible json, posts it to <http-address> and prints the response with some additional info (row_number and true label)
