import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import pywt

class Function():
    def __init__(self, t, a, Fs):
        self.time = t
        self.amplitude = a
        self.Fs = Fs

    
class Math(): 
    @staticmethod   
    def time_domain(sig):
       return sig.time, sig.amplitude

    @staticmethod
    def frequency_domain(sig, cut_0 = False):
        if cut_0:
            signal_frequencies = np.fft.fft(sig.amplitude)
            frequency = np.fft.fftfreq(sig.time.size, 1/sig.Fs)
            signal_frequencies = signal_frequencies[:int(-len(frequency)/2)]
            frequency = frequency[:int(len(frequency)/2)]
        else:
            signal_frequencies = np.fft.fft(sig.amplitude)
            frequency = np.fft.fftfreq(sig.time.size, 1/sig.Fs)
        return frequency, abs(signal_frequencies)

    @staticmethod
    def stft(sig, win, persek, overlap, _nfft):
        f, t, Zxx = signal.stft(sig.amplitude, sig.Fs, window=win, nperseg=persek, noverlap=overlap, nfft=_nfft)
        return t, f, np.abs(Zxx)

    @staticmethod
    def cwt(sig, scMin, scMax, wavelet):
        coef, freqs = pywt.cwt(sig.amplitude, np.arange(scMin,scMax), wavelet, sampling_period=sig.Fs)
        return sig.time, freqs, coef.real