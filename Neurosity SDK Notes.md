
## Purpose of the SDK: 

-The SDK connects your Python code to a Neurosity headset. There are 2 main headsets which are:
    - **Crown**: the newer model, sits around the head like a crown.
    ![[Pasted image 20250816145646.png]]
    - **Notion**: the older model, looks more like headphones.  
        Both measure brain signals (EEG) through small sensors on your head.
     ![[Pasted image 20250816145833.png]] 

- The SDK can handle:
    
    - **Authentication**: (More details below)
					Logging in with your Neurosity account so the device trusts your program.
					In order to stream data, the Neurosity OS to require authentication and authorization. 
					
    - **Device selection**: picking which headset you are connecting to.
    - **Streaming data**: sending brain signals and related information in real time into your code.

- The SDK gives you access to:
    1. Raw EEG signals ------> the brain’s electrical activity
    2. Frequency features (brainwaves like **delta**, **theta**, **alpha**, **beta**, **gamma**) -> Will be discussed further down. 
    3. Built-in mental states:
        - **Calm**: how relaxed you are. It’s high when you’re peaceful, quiet, or meditating.
        - **Focus**: how concentrated you are. It’s high when you are paying attention, solving problems, or working hard.  
            Calm and Focus are different: you can be calm but not focused (daydreaming), or focused but not calm (stressed).
    - **Motion** data from the accelerometer (detects when your head moves).
    - **Device information** (battery, charging, online status).

### Authentication and Device Setup: 

- `device_id`: found in the Neurosity mobile app under Device Info. In our case:(Dr Amjad gave it to us.)
- Required before subscribing to any data streams.
![[Pasted image 20250816150414.png]]
 

----- 
## Data Streams: 


### Sampling Rate: 
Every device has a specific sampling rate: 
- Crown :256Hz
- Notion 2 -> 250Hz
- Notion 1 -> 250Hz
**Note**: A sampling rate of 250Hz means the data contains 250 samples per second.
### Metrics: 
(Notes for Sara and Amr: each metric has more details in it, which we can review during the meeting.) 
- raw: **time-domain** EEG, filtered.
    - Use for your own DSP or time-domain features.
![[Pasted image 20250816153558.png]]
The `raw` brainwaves parameter emits events of 16 samples for Crown and 25 for Notion 1 and 2. We call these groups of samples **Epochs**. 
- `def callback(data): ...`  
    A function the SDK will call every time a raw EEG epoch arrives.
- `unsubscribe = neurosity.brainwaves_raw(callback)`  
    Subscribes to the raw EEG stream and starts pushing epochs into your callback.  
    Save the returned function in `unsubscribe`—call it later to stop streaming.


- `data["ts"]` or `data["timestamp"]`: when this epoch was produced (milliseconds since epoch).
- `data["data"]`: a 2-D array **channels × samples_per_epoch**.
    
    - On Crown, sample rate is **256 Hz** and the SDK sends 16 samples/channel per epoch (~62.5 ms per epoch).
- Optional fields (SDK/version dependent): `channelNames`, `samplingRate`, `info`.
    
**For example** :
- If you have 8 channels, `data["data"]` will look like `[[s11, s12, ..., s1N], [s21, ...], ...]` with `N=16`.
    
##### When or why we use raw ? 
- You want to do your own preprocessing. 
- Compute time-domain features. 
- Or build your own PSD. 

## (MORE RESEARCH TO BE DONE REGARDING THE REST OF THE METRICS)

rawUnfiltered: **time-domain** EEG before device filters.
    - Use for complete control of filtering.

- psd (Power Spectral Density): **frequency** distribution of power (μV²/Hz).
    - Use for frequency features, entropy, ratios.
    
- powerByBand: absolute band powers for **delta, theta, alpha, beta, gamma.**
    - Use for quick features without FFT.

### Other Streams
- **quality**: signal quality per electrode.
    - Use to reject noisy windows.
        
- **accelerometer**: head motion (X, Y, Z).
    - Use to detect movement artifacts.

- **calm**: built-in relaxation probability.
- **focus**: built-in attention probability.
- **kinesis**: trained commands for thought-based control.
- **status / device_info**: battery, charging, online state, firmware.


------ 
### Nuerology summary (to be updated)
Our brain cells (neurons) send tiny electrical signals. When many fire together, they make patterns called **brainwaves**. Different brainwaves happen at different speeds, and they tell us about what the brain is doing.

-> Our brain cells, **neurons**, send tiny electrical signals. When a neuron receives input, it creates tiny electrical changes **(postsynaptic potentials).**
    
-> Many neurons line up. In the **outer** layer of the brain (**cortex**), large groups of **pyramidal neurons** point in roughly the same direction. When they are active together (**synchrony**), their tiny signals add up.
    
->The headset sees the sum. The electrodes on the scalp pick up the _combined_ signal from thousands to millions of neurons under each sensor. We measure this in **microvolts**.

->Brain circuits have “**pacemakers” and feedback loops**. When groups of neurons speed up or slow down together, we see **oscillations** at different speeds (frequencies).
    
->The **PSD** shows how much of the signal’s energy sits at each frequency. **Band power** is the energy in a range (e.g., alpha 8–12 Hz).

General note: 
If there is more synchrony : there is higher power at that frequency 
If there is more **desynchrony**: then there is lower power at that frequency. 

#### What each band reflects : The 5 types of brainwaves 

Very good source to read more:
https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/brain-waves 

![[Pasted image 20250816152411.png]]
#### 1. Delta (0.5–4 Hz)

- Very slow “up–down” cycles in the cortex. Strong in deep, dreamless sleep (N3). During waking, high delta usually means drowsiness, eye movements, or drift.
- **Why does it change? :** 
				- Big, slow waves need large groups of neurons to rise and fall together.

Extra note: Rising delta during tasks can signal fatigue or eye-movement artifacts. Usually in research, they reject windows with very high delta unless they are studying sleep.
    

#### 2. Theta (4–8 Hz): 

![[Pasted image 20250816152752.png]]
-  In adults, **frontal** **midline theta** appears during sustained mental effort and error monitoring (medial prefrontal/anterior cingulate circuits). In the hippocampus, theta supports memory and navigation (scalp sees this only weakly).
    
- **Why it changes? :**
			When the brain internally focuses (working memory, mental math, meditation), small networks synchronize at theta.

#### Alpha (8–12 Hz)

 A thalamo-cortical “idling/gating” rhythm; strongest over visual areas with **eyes closed**. It often **drops** when you open your eyes or engage with a task.
    
- **Why it changes ?:**
				When the brain “gates out” external input (rest, closed eyes), neurons synchronize at alpha. When you attend to the world, those neurons desynchronize, so alpha power falls.
    
    - Higher alpha → relaxation/low arousal; Calm.
    - **Alpha suppression** ( a drop) → **attention/arousal**.
    - **Frontal Alpha Asymmetry (FAA)** (left vs right alpha) is used as a **valence** proxy: 
    relatively **lower alpha** (so more activation) on the **left** frontal side is often linked to **approach/positive** tendencies; relatively lower on the **right** to **withdrawal/negative**.
        

#### Beta (12–30 Hz)

Faster rhythms shaped by **sensorimotor** and **frontoparietal** loops; influenced by inhibitory interneurons and basal ganglia–cortical circuits. Increases with active thinking and motor preparation.
- **Why it changes? :**
			Goal-directed processing and muscle tension both **push energy** into beta/high-beta.
    - **Higher beta** → **alertness/task engagement** --> can also rise with stress.
    - Extra note:  jaw/forehead muscle tension can inflate high-beta.
        

#### Gamma (30–100 Hz)

Very fast local networks (usually they are driven by **parvalbumin interneurons**) that help tie features together during perception and learning. Mostly local and weak on the scalp.
    
- **Why it changes ?:** 
			-When neurons in a small area work together very quickly, gamma power rises.

    - Useful for **sensory processing** and some **high-arousal** states, but it is **easily contaminated by EMG** ->(tiny face/eye muscles).
    - Broad band Gamma is usually handled with caution!



##### Terms to further look into :
( FOR AMR: Here I just briefly understood the terms, but I am digging deeper into the terms via articles and videos)
- Oscillation: repeating up-down electrical pattern.
- Synchrony: many neurons oscillate together; increases band power.
- Desynchrony (ERD): neurons work independently during active processing; this usually lowers alpha.
- PSD: power at each frequency.
- Absolute/Relative band power: energy in a band before/after normalization.
- Artifact: non-brain signal (eyes, muscles, motion, mains noise).


##### References: 
https://docs.neurosity.co/docs/overview/
https://github.com/neurosity/neurosity-sdk-python 
https://www.geeksforgeeks.org/electronics-engineering/power-spectral-density/ 

