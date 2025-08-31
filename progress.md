## *Roadmap*
  - Perform EDA (Exploratory Data Analysis) on the raw, absolute power, and psd data (with calm/focus probabilities)
  - Use decision trees / regression for Feature Importance Analysis
  - ***Phase 1***
    - Train Supervised Learning Algorithms such as Classification, Boosting, and Bagging
  - ***Phase 2***
    - Train LLM
## *Currently Working On*
- [ ] Add Labels (what do we want to predict) (Wait For Meeting with Dr.Amjad)
### Notebooks
- [ ] Documentation for capabilities and limitations of consumer-grade EEG (Amr)
- [ ] Cleaning Up [sdkTest](src/python/notebooks/SDKtest.ipynb) and add explanation for all epochs being recieved (Sarah)
### Data Scripts
- [ ] Aggregate Features (Amr)
  - research more about ratios and what they mean
- [x] Adding proper documentation to the scripts (Amr)
- [x] Scaling the data_retrieval script so its can do checkpoint saves & doesn't just erase what's already in the csv (Sarah)
- [x] Dropping Nulls (Amr)
- [ ] retrieve raw data in new script where it stores all the samples for one second and compresses them, allowing them to be added in preprocessing.py
### SDK
- [x] Understand and explain PSD functions in SDK (Sarah)
- [ ] check the kinesis functions available in SDK (Sarah)
## *Issues / Pending*
- SDK AP function timestamp unavailable
- [x] choose a unique datetime instead of H:M:S
