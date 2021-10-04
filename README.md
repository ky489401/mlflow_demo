MLFlow Demo
----

Minimal example to demonstrate basic mlflow features. 

The following items are logged in the demo for reproducibility:

* model hyper-parameters
* evaluation metrics 
* dataset 
* fitted model 
* git commit hash 

The MLFlow UI allows us to compare models based on eval metrics etc.  

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

## UI 
should look like this...
![alt text](https://www.google.com/url?sa=i&url=https%3A%2F%2Fpycaret.org%2Fmlflow%2F&psig=AOvVaw3RTyHvX7TEqetW1XxoCYHU&ust=1633472991979000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNDU2Z3nsfMCFQAAAAAdAAAAABAD) 