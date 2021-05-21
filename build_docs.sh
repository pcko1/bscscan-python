#!/bin/bash
clear
rm -r build/*
sphinx-apidoc -f -o source bscscan
make html