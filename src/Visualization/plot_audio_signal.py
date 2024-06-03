
import matplotlib.pyplot as plt

def plot_audio_signal(data):
    plt.figure()
    plt.plot(data)
    plt.xlabel("Sample index")

    plt.ylabel("Amplitude")

    plt.title("Waveform of test Audio")

    plt.show()
