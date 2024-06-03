import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read,write
from IPython.display import Audio
from numpy.fft import fft, ifft
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname('../Visualization/plot_audio_signal.py'))

SCRIPT_DIR2 = sys.path.append(os.path.dirname('../Filters/band-pass_filter.py'))

from plot_audio_signal import plot_audio_signal
from band_pass_filter import band_pass_filter

Fs , data = read('../../Data/Actor_01/03-01-01-01-01-01-01.wav')

low_cutoff = 500  # Example: 500 Hz
high_cutoff = 2000  # Example: 2000 Hz

filtered_data = band_pass_filter(data[:] , low_cutoff,high_cutoff , Fs)

print("Sampling frecuency is: ",Fs)


print("Figure out how the audio data representation look like: ",filtered_data)

print("Size of the audio list: ",len(filtered_data))

plot_audio_signal(filtered_data)

