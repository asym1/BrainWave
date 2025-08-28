## *Roadmap*
  - Perform EDA (Exploratory Data Analysis) on the raw, absolute power, and psd data (with calm/focus probabilities)
  - Use decision trees / regression for Feature Importance Analysis
  - ***Phase 1***
    - Train Supervised Learning Algorithms such as Classification, Boosting, and Bagging
  - ***Phase 2***
    - Train LLM
## *Currently Working On*
- Recording and saving data
  - Fixing the sampling rate mismatch: timestamp only counts seconds not milliseconds since we only get one calm/focus per second, then we find the mean of all ap in one second and add the column to the column with ap NaN but p_focus/calm
  - Resampling to a fixed time step
  - Aggregate Features
  - Add Labels
- Adding proper documentation to the scripts
- Scaling the data_retrieval script so it can do checkpoint saves & doesn't just erase what's already in the csv
## *Issues / Pending*