import pandas as pd
import numpy as np
import ast

# Load CSV with collected rows
table = pd.read_csv('./data/collected/ap_probability.csv')

# Turn Array Columns from object type to string type so i can parse them to lists later
table = table.astype({'alpha': 'string', 'beta': 'string','delta': 'string','gamma': 'string','theta': 'string'})

# Parse Array Strings -> List -> Np Arrays
for col in ["alpha", "beta", "delta", "gamma", "theta"]:
    table[col] = table[col].apply(lambda x: np.array(ast.literal_eval(x)) if isinstance(x, str) else x) # turn string -> list -> nparray or if NaN -> NaN

def array_mean(x): # stack arrays and then get the mean row-wise 
                   # (allows the multiple rows of the same second to turn to one)
    arrays = [array for array in x if isinstance(array, np.ndarray)]
    if not arrays:
        return np.nan
    return np.nanmean(np.vstack(arrays), axis=0)

table = table.groupby("timestamp").agg({ # Final Group-By that compresses collected samples and sets the table to 1Hz
    "alpha": array_mean, # mean of all rows with the same second
    "beta": array_mean, # mean of all rows with the same second
    "delta": array_mean, # mean of all rows with the same second
    "gamma": array_mean, # mean of all rows with the same second
    "theta": array_mean, # mean of all rows with the same second
    "p_focus": "mean", # normal scalar mean
    "p_calm": "mean" # normal scalar mean
})

# Drop NaNs
table = table.dropna()

# Feature Engineering for Aggregate Features and more

# Emotions/States Labelling (for training set)

# Saving CSV
table.to_csv('./data/processed/ap_probability_clean.csv')