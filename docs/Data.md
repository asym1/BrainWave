## Epoch
- instead of streaming one sample at a time (at 256 samples a second), the API groups 16 samples into a mini-window called an *epoch*, allowing you to recieve 16 epochs per second, with each `epoch = 16 samples / 256 Hz = 62.5 ms` worth of data.

Why use epochs instead of single samples?
- More efficient for streaming.
- Easier to process in small blocks (e.g., for FFT or feature extraction).
- Keeps timing consistent.

## Raw Data
Check the Brainwaves theory for an explanation of the EEG data and how to interpret it. This section will explain the different Noise & Artifacts that can show up in the raw data
### Raw unfiltered
- EEG data without any processing, filtering, or cleaning
- conains the neural activity, but also enviromental electrical noise, DC drift, and muscle/eye/movement artifacts
- the filtered version is usually better for ML & analysis
### Noise
- 
### Artifacts
- 
---
## Absolute Power By Band
- Absolute power is the amount of activity within a specific frequency band of brain waves, usually ordered from slowest to fastest

- 
## PSD Symmetry
- Power Spectral Density (PSD) is an effective method to differentiate between noise and features in a signal by showing how much power is in different frequency bands. One of the most common features extracted from EEG because brain states modulate the power of certain frequency bands (e.g. high alpha = relaxed, beta busts in motor cortex = preparing to move)
- the meaning of Symmetry in PSD symmetry is for comparing electrode pairs that are mirrored across the head
	- C3, C4 (motor cortex, left vs right)
	- CP3, CP4. CP5, CP6 (central-parietal areas, left vs right)
	- F5, F6 (frontal, left vs right)
- A ratio close to one shows symmetry, while a deviation equals lateralization, which might show that a left hand is moving for example, or if left activity is stronger in frontal then that might mean positive activity while right is linked with negative (just an example, not fact)

```python
def callback(data):
    print("data", data)

unsubscribe = neurosity.brainwaves_psd(callback)
```
- code above outputs new epochs 4 times a second, eith every frequency label containing the computed FFT (fast fourier transform) value per channel (`psd` propertry), as well as the frequency ranges (`freqs` property)
## References
https://www.researchgate.net/figure/Absolute-Power-amount-of-activity-within-a-specific-frequency-band-of-brain-waves-in_fig2_343527156
