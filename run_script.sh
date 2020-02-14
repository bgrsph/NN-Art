#!/bin/bash

# $1: Content Image Path
# $2: Style Image Path
# $3: Output Image Name (with format)
# $4: Number of iterations

#conda activate neuralStyle
python neural_style.py --content $1 --styles $2 --output $3 --iterations $4 --overwrite
#conda deactivate
exit 0
