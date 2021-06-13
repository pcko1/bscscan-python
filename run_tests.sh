#!/bin/bash
clear
export API_KEY=$1
pip install coverage
coverage run -m unittest discover && coverage report -m