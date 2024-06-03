import numpy as np
from numpy.fft import fft, ifft

def band_pass_filter(data, low_cutoff, high_cutoff, Fs):

    fft_data = fft(data)
    
    freqs = np.fft.fftfreq(len(data), 1 / Fs)
    
    filter_mask = (np.abs(freqs) >= low_cutoff) & (np.abs(freqs) <= high_cutoff)
    
    fft_data = fft_data * filter_mask
    
    filtered_data = np.real(ifft(fft_data))
    
    return filtered_data