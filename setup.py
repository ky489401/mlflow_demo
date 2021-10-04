#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = ["wheel", "mlflow", "loguru", "sklearn"]

setup(
    author="Kelvin Yeung",
    python_requires=">=3.5",
    description="mlflow demo",
    install_requires=requirements,
    name="mlflow_demo",
    test_suite="tests",
    version="0.1.0"
)
