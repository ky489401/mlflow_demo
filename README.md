MLFlow Demo
----

Minimal example to demonstrate mlflow functionalities. 

The following things are logged in the dummy experiment:

* model hyper-parameters
* evaluation metrics 
* dataset 
* fitted model 
* git commit hash 

The MLFlow UI allows us to compare models based on eval metrics, for example.  

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