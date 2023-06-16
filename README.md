# mlcourse-final-project

Project description:


Dataset info:<br>
Physical Activity Monitoring dataset<br>
https://archive.ics.uci.edu/dataset/231/pamap2+physical+activity+monitoring<br>
more detainls in dataset_readme.pdf<br>

## API description


## How to run the app
Setup and run:
From mlcourse-final-project directory run the following commands
```
docker duild -t pamap_app .
docker run --rm -dp 5678:5678 --name pamap-app-container pamap_app:latest
```
Note that the first command must run from mlcourse-final-project directory.

Stop and delete:
```
docker stop pamap-app-container
```

## How to use example_client
```
python path/to/example_client/example_client.py <http-address> [row_number]
```
http address for current app configuration: http://localhost:5678

row_number: any nonnegative integer to take row_number'th row from smallest_sample_for.test<br>
if not specified row_number is chosen randomly, if exceeds test data length row_number = row_number % data_len<br>
The client chooses random (if not specified otherwise) row from smallest_sample_for.test, converts it into API-compatible json, posts it to <http-address> and prints the response with some additional info (row_number and true label)