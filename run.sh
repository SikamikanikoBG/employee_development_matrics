#!/bin/bash
DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "$DIR"

# Activate Conda environment
source /home/anakin/anaconda3/bin/activate data_portal

# Start the API
nice -n 16 streamlit run "$DIR/main.py" --server.port 8504
