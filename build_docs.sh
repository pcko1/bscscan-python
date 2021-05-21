#!/bin/bash
rm -r build/*
clear
sphinx-apidoc -f -o source bscscan
make html