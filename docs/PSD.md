PSD

- Power Spectral Density (PSD) represents how the power of a signal is distributed across different frequency components.
- Used as a frequency domain analysis tool. 
- PSD indicates which frequencies carry more energy.
- PSD is used to analyze signals contaminated by noise or containing multiple oscillatory components.

Very important source that we can always refer back to: https://matplotlib.org/stable/gallery/lines_bars_and_markers/psd_demo.html#sphx-glr-gallery-lines-bars-and-markers-psd-demo-py 

Matplotlib allows you to compute and compare power spectral density estimates using two methods:
1. **Periodogram** 
2. **Welch’s method**


## 1. Welch's method : 
Matplotlib implements PSD computation based on Welch’s method. There are two main interfaces:

1. **`matplotlib.pyplot.psd()`** : 
    - A direct plotting function that computes and displays the PSD of an input signal.
    Arguments: 
        - `x`: Array or sequence containing the data. 
        - `NFFT`: No. of data points used for each block in the FFT.
        - `Fs`: Sampling frequency of the signal.
        - `detrend`, `window`, `noverlap`: Options for preprocessing.


![[Pasted image 20250831123609.png]]
Source: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.psd.html# 
This source includes detailed explanations on the arguments above. 


 2. **`Axes.psd()`**
    
    - An object-oriented variant, called on an `Axes` object.
    - Provides the same functionality, but integrates into subplot management more flexibly.
- ![[Pasted image 20250831123923.png]]

Source:https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.psd.html 


## How PSD can help in EEG and Brainwave Data Analysis: 

#### 1. Decompose the signals to check dominating brainwave: 
- PSD can decompose eeg signals into their frequency components (delta, theta, alpha, beta, gamma). This allows you to see which brainwave band carries the most power at a given time.
- For example, if alpha is high, this can indicate a calm state. 
