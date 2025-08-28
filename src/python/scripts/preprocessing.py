import pandas as pd
import numpy as np
import ast

# Load CSV
table = pd.read_csv('./data/collected/ap_probability.csv')
print(table.head())

# Turn Array Columns from object type to string type
table = table.astype({'alpha': 'string', 'beta': 'string','delta': 'string','gamma': 'string','theta': 'string'})
# Parse Array Strings into Arrays
for col in ["alpha", "beta", "delta", "gamma", "theta"]:
    table[col] = table[col].apply(lambda x: np.array(ast.literal_eval(x)) if isinstance(x, str) else x) # turn string -> list -> nparray or if NaN -> NaN

def array_mean(x): # stack arrays, mean row-wise
    arrays = [array for array in x if isinstance(array, np.ndarray)]
    if not arrays:
        return np.nan
    return np.nanmean(np.vstack(arrays), axis=0)

table = table.groupby("timestamp").agg({
    "alpha": array_mean,  
    "beta": array_mean,   
    "delta": array_mean,
    "gamma": array_mean,
    "theta": array_mean,
    "p_focus": "mean", # normal scalar mean
    "p_calm": "mean"
})

# Feature Engineering for Aggregate Features and more

# Emotions/States Labelling (for training set)

# Saving CSV
table.to_csv('./data/processed/ap_probability_clean.csv')