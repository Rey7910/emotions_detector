import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read,write
from IPython.display import Audio
from numpy.fft import fft, ifft
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname('../Visualization/plot_audio_signal.py'))

from plot_audio_signal import plot_audio_signal

Fs , data = read('../../Data/Actor_01/03-01-01-01-01-01-01.wav')

data = data[:]

print("Sampling frecuency is: ",Fs)


print("Figure out how the audio data representation look like: ",data)

print("Size of the audio list: ",len(data))

plot_audio_signal(data)

