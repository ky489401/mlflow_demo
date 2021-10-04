import os
import pickle

import mlflow
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# https://github.com/mlflow/mlflow-example/blob/master/train.py
# https://www.mlflow.org/docs/latest/quickstart.html

def save_as_pickle(path, save_object):
    with open(path, "wb") as f:
        pickle.dump(save_object, f)

if __name__ == "__main__":

    # load dataset
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    # train classification model
    penalty = "l2"  # regularisation param
    clf = LogisticRegression(penalty=penalty).fit(X, y)

    # predict
    y_pred = clf.predict(X)

    # log a model hyper-parameter
    mlflow.log_param("penality", penalty)

    # log an evaluation metric
    accuracy = accuracy_score(y_true=y, y_pred=y_pred)
    mlflow.log_metric("accuracy", accuracy)

    # log datasets and the trained model as artefacts
    model_dir = "artefacts"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    dataset_path = os.path.join(model_dir, "dataset.pkl")
    model_path = os.path.join(model_dir, "model.pkl")

    save_as_pickle(save_object=iris, path=dataset_path)
    save_as_pickle(save_object=iris, path=model_path)

    mlflow.log_artifacts(model_dir)

    # git commit hash is logged to server too
