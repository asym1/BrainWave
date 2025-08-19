# BrainWave
EEG emotion detection in Python

# Getting Started
## File Structure
- The *data* folder will contain a folder for raw data recieved from the emulator, as well as processed training data
- The *models* folder will store all model's that have been trained (using PyTorch)
- The *src* folder will contain all the project's scripts for preprocessing, cleaning, and training/predictions
- The *docs* folder will contain theory on brainwaves as well as intuition on different scripts in src
- The *progress* file will have the list of current tasks we are working on for convenience and any future open source contributions
## Setup
- Create a `.env` file with the Neurosity Emulator: Device Id, account Email, account Password
```
NEUROSITY_EMAIL=your email here
NEUROSITY_PASSWORD=your password here
NEUROSITY_DEVICE_ID=your device id here
```
- Setup a virtual enviroment and ide to allow jupyter notebooks & python scripts
- install everything in `requirements.txt` using either pip or enviroment command
- Go to [SDK Testing Notebook](src/python/notebooks/SDKtest.ipynb) to make sure your sdk is working properly before using any scripts in the following sections
