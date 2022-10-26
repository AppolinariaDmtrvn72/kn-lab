
# train

download dataset [gtsrb](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)
 and 
unpack Train folder from dataset to ./data/

run train with `python3 traffic.py data_folder model_file_name.h5`

# service


run server with `python3 server.py`

go to `http://0.0.0.0:8000/docs` and "Try out" request with one of dataset pictures
