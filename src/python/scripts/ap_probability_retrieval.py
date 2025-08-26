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


load_dotenv()

# Connect to Neurosity
neurosity = NeurositySDK({
    "device_id": os.getenv("NEUROSITY_DEVICE_ID")
})
neurosity.login({
    "email": os.getenv("NEUROSITY_EMAIL"),
    "password": os.getenv("NEUROSITY_PASSWORD")
})

# Variables
seconds = 5

# Callbacks for the SDK
def callback_focus(data):
    pass
def callback_calm(data):
    pass
def callback_ap(data):
    pass

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

pass 

