MLFlow Demo
----

Minimal example to demonstrate basic mlflow features. 

The demo loads a dataset, trains a model, and logs the following items to mlflow for reproducibility: 

* model hyper-parameters
* evaluation metrics 
* dataset 
* fitted model 
* git commit hash 

We can then view and compare experiments with mlflow's interactive UI.

##  Setup

* `git clone https://github.com/ky489401/mlflow_demo.git`
* `cd mlflow_demo` 
* setup virtual env 
    * `python3 -m venv venv`
    * `source venv/bin/activate`
* install dependencies `pip install -e .`

## Run Demo 
* `cd src/` 
* run demo `python demo.py`
* setup mlflow tracking UI `mlflow ui`
* access UI at `http://127.0.0.1:5000`