import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read,write
from IPython.display import Audio
from numpy.fft import fft, ifft
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname('../Visualization/plot_audio_signal.py'))

SCRIPT_DIR2 = sys.path.append(os.path.dirname('../Filters/low-pass_filter.py'))

from plot_audio_signal import plot_audio_signal
from low_pass_filter import low_pass_filter

Fs , data = read('../../Data/Actor_01/03-01-01-01-01-01-01.wav')

cutoff_frequency = 1000

filtered_data = low_pass_filter(data[:] , cutoff_frequency , Fs)

print("Sampling frecuency is: ",Fs)


print("Figure out how the audio data representation look like: ",filtered_data)

print("Size of the audio list: ",len(filtered_data))

plot_audio_signal(filtered_data)

