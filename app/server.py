import os

import pickle
import pandas as pd

from activity_dict import activity_dict
from lightgbm import LGBMClassifier

from flask import Flask, jsonify, request


files_dir = '../pickles'

with open(os.path.join(files_dir, 'pipe.pkl'), 'rb') as pipe_file:
    pipe = pickle.load(pipe_file)

with open(os.path.join(files_dir, 'boosting_model.pkl'), 'rb') as bst_file:
    classif = pickle.load(bst_file)

with open(os.path.join(files_dir, 'clustering_model.pkl'), 'rb') as clust_file:
    kmeans = pickle.load(clust_file)

with open(os.path.join(files_dir, 'dropcols.txt'), 'r') as cols_file:
    s = cols_file.read()
cols_to_drop = [col for col in s.split(', ')]

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    data = request.get_json()
    to_predict = pd.DataFrame(data, index=[0])

    to_predict['clusters'] = kmeans.predict(
        pipe.transform(to_predict.drop(columns=cols_to_drop))
    )
    preds = classif.predict_proba(to_predict)[0]
    answer = {activity_dict[i]: preds[i] for i in range(len(preds))}
    return jsonify(answer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5678)