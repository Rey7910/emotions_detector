import numpy as np
import matplotlib.pyplot as plt

def plot_audio_signal(time, signal, title="Audio Signal", xlabel="Time [s]", ylabel="Amplitude"):
    """
    Plots the audio signal.

    Parameters:
    - time: array-like, the time points corresponding to the signal values
    - signal: array-like, the audio signal values
    - title: str, the title of the plot
    - xlabel: str, the label for the x-axis
    - ylabel: str, the label for the y-axis
    """
    plt.figure(figsize=(15, 5))
    plt.plot(time, signal)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


time = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 5 * time)

# Call the plotting function
plot_audio_signal(time, signal, title="Example Audio Signal", xlabel="Time [s]", ylabel="Amplitude")