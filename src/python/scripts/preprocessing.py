import pandas as pd
import numpy as np

# Load CSV
table = pd.read_csv('./data/collected/ap_probability.csv')
print(table.head())

# Fixing Timestamps (sampling rate mismatch)
##  Resampling to a fixed time step
##  Filling NaNs

# Feature Engineering for Aggregate Features and more

# Emotions/States Labelling (for training set)