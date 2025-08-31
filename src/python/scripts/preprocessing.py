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

# Final Group-By that compresses collected samples and sets the table to 1Hz
table = table.groupby("timestamp").agg({ 
    "alpha": array_mean, "beta": array_mean, "delta": array_mean, "gamma": array_mean, "theta": array_mean, # mean of all rows with the same second
    "p_focus": "mean", "p_calm": "mean" # normal scalar mean
})

# Drop NaNs
table = table.dropna()

# Feature Engineering for Aggregate Features and more
columns = ['alpha', 'beta', 'delta', 'gamma', 'theta']
channels = ['CP6', 'F6', 'C4', 'CP4', 'CP3', 'F5', 'C3', 'CP5'] # derived from testing in sdkTest

# New Columns with mean, varience, max, and min power for alpha, beta, etc.
for col in columns:
    table[f'mean_{col}'] = table[col].apply(lambda x: np.mean(x))
    table[f'varience_{col}'] = table[col].apply(lambda x: np.var(x))
    table[f'max_{col}'] = table[col].apply(lambda x: np.max(x))
    table[f'min_{col}'] = table[col].apply(lambda x: np.min(x))

# New Columns seperating bands by channel
for col in columns:
    for i, ch in enumerate(channels):
        table[f'{col}_{ch}'] = table[col].apply(lambda x: x[i])

# Sum across channels for each band
for col in columns:
    table[f'{col}_sum'] = table[col].apply(sum)

# Total power across all bands
table['total_power'] = table[[f'{col}_sum' for col in columns]].sum(axis=1)

# Relative power per band
for col in columns:
    table[f'relative_{col}'] = table[f'{col}_sum'] / table['total_power']

# Emotions/States Labelling (for training set)

# Saving CSV
table.to_csv('./data/processed/ap_probability_clean.csv')