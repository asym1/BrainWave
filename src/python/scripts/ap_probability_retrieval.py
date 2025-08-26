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
currTimestamp = 0

# Callbacks for the SDK
def callback_focus(data):
    global focusList
    global currTimestamp 
    currTimestamp = data['timestamp']
    focusList.append([data['timestamp'], {data['label']: data['probability']}])
def callback_calm(data):
    global calmList
    global currTimestamp 
    currTimestamp = data['timestamp']
    calmList.append([data['timestamp'], {data['label']: data['probability']}])
def callback_ap(data):
    global apList
    global currTimestamp
    apList.append([currTimestamp, data['data']['alpha'], data['data']['beta'], data['data']['delta'], data['data']['gamma'], data['data']['theta']])

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
print(focusList)
print(calmList)
print(apList)
