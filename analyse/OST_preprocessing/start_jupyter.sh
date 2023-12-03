#!/bin/sh
mamba activate male
python3 -m ipykernel install --user --name OpenData
jupyter lab .
