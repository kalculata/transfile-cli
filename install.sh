#!/bin/bash

echo "Uninstall previous versions"
pip uninstall transfile -y

echo "Build package"
python setup.py sdist bdist_wheel

echo "Install package"
pip install .
