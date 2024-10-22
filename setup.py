from setuptools import find_packages, setup
from typing import List


setup(
    name='ChargePrediction',
    version='0.0.1',
    author='Tushar Rohilla',
    author_email='tusharrohilla70@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)