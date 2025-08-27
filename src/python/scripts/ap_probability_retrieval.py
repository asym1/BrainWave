# all necessary imports for data retrieval and storage
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from neurosity import NeurositySDK

from dotenv import load_dotenv
import os
# might need to avoid writing into same table at the same time (data corruption)
# import threading

# Connecting To Neurosity
load_dotenv()
neurosity = NeurositySDK({
    "device_id": os.getenv("NEUROSITY_DEVICE_ID")
})
neurosity.login({
    "email": os.getenv("NEUROSITY_EMAIL"),
    "password": os.getenv("NEUROSITY_PASSWORD")
})

# Variables
seconds = 5
focusList = []
calmList = []
apList = []

# Callbacks for the SDK
def callback_focus(data):
    global focusList
    focusList.append([data['timestamp'],data['probability']])
def callback_calm(data):
    global calmList
    calmList.append([data['timestamp'], data['probability']])
def callback_ap(data):
    global apList
    ts = int(time.time() * 1000)
    apList.append([ts, data['data']['alpha'], data['data']['beta'], data['data']['delta'], data['data']['gamma'], data['data']['theta']])

# Subscriptions to the live stream
print(f"collecting data for the ap_probability table for {seconds} seconds")
focus_unsubscribe = neurosity.focus(callback_focus)
calm_unsubscribe = neurosity.calm(callback_calm)
ap_unsubscribe = neurosity.brainwaves_power_by_band(callback_ap)

# Duration of live stream
time.sleep(seconds)

# Stop Subscription
focus_unsubscribe()
calm_unsubscribe()
ap_unsubscribe()

# Save to csv
apList = pd.DataFrame(apList, columns=["timestamp","alpha","beta","delta","gamma","theta"])
calmList = pd.DataFrame(calmList, columns=["timestamp", "p_calm"])
focusList = pd.DataFrame(focusList, columns=["timestamp", "p_focus"])

ap_probability_table = pd.merge(apList, calmList, on="timestamp", how="outer")
ap_probability_table = pd.merge(ap_probability_table, focusList, on="timestamp", how="outer")
ap_probability_table.index = pd.to_datetime(ap_probability_table["timestamp"], unit="ms", utc=True).dt.strftime("%H:%M:%S.%f").str[:-1]
ap_probability_table = ap_probability_table.drop(columns=["timestamp"])
ap_probability_table.to_csv('./data/collected/ap_probability.csv')
