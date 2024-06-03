import numpy as np
from numpy.fft import fft, ifft

def low_pass_filter(data, cutoff_frequency, Fs):

    fft_data = fft(data)
    
    freqs = np.fft.fftfreq(len(data), 1 / Fs)
    
    fft_data[np.abs(freqs) > cutoff_frequency] = 0
    
    filtered_data = np.real(ifft(fft_data))
    
    return filtered_data