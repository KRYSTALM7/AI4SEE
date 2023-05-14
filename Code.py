'''
a) Read the data from the CSV file consisting of a single column named 'data'.
 The plot of this data is shown in the image attached to this assignment.
b) Write the Python code to detect the number of positive peaks in the waveform
c) Perform necessary preprocessing operations if required
'''
#importing required libraries
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
df = pd.read_csv(r'S:\CODING NOTES\PYTHON3.0\CSV files\data_file.csv')
print(df)
import matplotlib.pyplot as plt
print(plt.plot(df))
waveform = df['data'].to_numpy()
# Find the peaks in the waveform
peaks, _ = find_peaks(waveform, prominence=0.5)
# Plot the waveform and the detected peaks
plt.plot(waveform)
plt.plot(peaks, waveform[peaks], "x")
plt.show()
# Count the number of peaks
num_peaks = len(peaks)
# Print the number of peaks
print("Number of Positive  peaks:", num_peaks)
