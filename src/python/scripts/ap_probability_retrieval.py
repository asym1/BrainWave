# all necessary imports for data retrieval and storage
import time
import pandas as pd
from neurosity import NeurositySDK
from dotenv import load_dotenv
import os

# Authenticating & Connecting To Neurosity
load_dotenv()
neurosity = NeurositySDK({
    "device_id": os.getenv("NEUROSITY_DEVICE_ID")
})
neurosity.login({
    "email": os.getenv("NEUROSITY_EMAIL"),
    "password": os.getenv("NEUROSITY_PASSWORD")
})

# Variables
seconds = 10000
focusList = []
calmList = []
apList = []
CSV_FILE = './data/collected/ap_probability.csv' 
BUFFER_LIMIT = 500
def save_checkpoint():
    
    global apList, calmList, focusList
    if not (apList or calmList or focusList): 
        return # If it is none of the states, nothing to save 
    
# Convert lists to DataFrames
    ap_df = pd.DataFrame(
        apList,
        columns=["timestamp", "alpha", "beta", "delta", "gamma", "theta"]
    )
    calm_df = pd.DataFrame(
        calmList,
        columns=["timestamp", "p_calm"]
    )
    focus_df = pd.DataFrame(
        focusList,
        columns=["timestamp", "p_focus"]
    )
       # Merge all three DataFrames
    merged = pd.merge(ap_df, calm_df, on="timestamp", how="outer")
    merged = pd.merge(merged, focus_df, on="timestamp", how="outer")

    # Format timestamp into datetime index
    merged.index = pd.to_datetime(
        merged["timestamp"], unit="ms", utc=True
    ).dt.strftime("%m/%d/%Y, %H:%M:%S")
    merged = merged.drop(columns=["timestamp"])

    # Append to CSV (write header only if file doesn't exist)
    file_exists = os.path.isfile(CSV_FILE)
    merged.to_csv(CSV_FILE, mode="a", header=not file_exists)
    print(f"Appended {len(merged)} Rows To ap_probability.csv")
    # Clear buffers
    apList, calmList, focusList = [], [], [] 

# Callbacks for the SDK
def callback_focus(data):
    global focusList
    focusList.append([data['timestamp'],data['probability']]) # adds samples as rows with the structure of [ts, p_f]
    if len(focusList) >= BUFFER_LIMIT:
        save_checkpoint() 
    
def callback_calm(data):
    global calmList
    calmList.append([data['timestamp'], data['probability']]) # adds samples as rows with the structure of [ts, p_c]
    if len(calmList) >= BUFFER_LIMIT:
        save_checkpoint()

def callback_ap(data):
    global apList
    ts = int(time.time() * 1000) # since the API doesn't send the ap's timestamp i use the system for it
    # adds samples as rows of [ts, alpha, beta, delta, gamma, theta]
    apList.append([ts, data['data']['alpha'], data['data']['beta'], data['data']['delta'], data['data']['gamma'], data['data']['theta']])
    if len(apList) >= BUFFER_LIMIT:
        save_checkpoint()

# Subscriptions to the live stream for focus, calm, and absolute power by band
print(f"collecting data for the ap_probability table for {seconds} seconds")
focus_unsubscribe = neurosity.focus(callback_focus)
calm_unsubscribe = neurosity.calm(callback_calm)
ap_unsubscribe = neurosity.brainwaves_power_by_band(callback_ap)

# Duration of live stream (execution delayes for s seconds)
time.sleep(seconds)

# Stop Subscription
focus_unsubscribe()
calm_unsubscribe()
ap_unsubscribe()

# # Turn all list into DataFrames with named columns for easy modification 
# apList = pd.DataFrame(apList, columns=["timestamp","alpha","beta","delta","gamma","theta"])
# calmList = pd.DataFrame(calmList, columns=["timestamp", "p_calm"])
# focusList = pd.DataFrame(focusList, columns=["timestamp", "p_focus"])

# # join all rows based on ts column so [ts, p_f] + [ts, p_c] + [ts, a, b, g, d, t] = [ts, a, b, g, t, d, p_f, p_c]
# ap_probability_table = pd.merge(apList, calmList, on="timestamp", how="outer")
# ap_probability_table = pd.merge(ap_probability_table, focusList, on="timestamp", how="outer")

# # Set index to datetime for auto sort and general convenience
# ap_probability_table.index = pd.to_datetime(ap_probability_table["timestamp"], unit="ms", utc=True).dt.strftime("%m/%d/%Y, %H:%M:%S")
# ap_probability_table = ap_probability_table.drop(columns=["timestamp"])

# # Save To CSV (needs to be changed to it adds to existing csv)
# ap_probability_table.to_csv('./data/collected/ap_probability.csv')

save_checkpoint() 