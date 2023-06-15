this client usage:

python ./example_client <http-address> [row_number]

http address for current app configuration: http://localhost:5678

row_number: any nonnegative integer to take row_number'th row from smallest_sample_for.test
if not specified row_number is chosen randomly, if exceeds test data length row_number = row_number % data_len

