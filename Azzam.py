
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd

ecg = pd.read_csv('ecg.csv')
x1=ecg.iloc[0:-1,0].values
y1=ecg.iloc[0:-1,1].values

eeg = pd.read_csv('001FN03.mat_EEG.csv')
y2=eeg.iloc[0:-1,0].values
x2=[]
for i in range (0,len(y2),1):
    x2.append(i)

emg1 = pd.read_csv('001FN03.mat_sEMG.extensors.csv')
y3=emg1.iloc[0:-1,0].values
x3=[]
for i in range (0,len(y3),1):
    x3.append(i)
fig=plt
def Signalplot (a,b,c,d,e,f):
    plt.subplot(2, 3, 1)
    plt.title("ECG")
    plt.xlabel('Time')
    plt.ylabel('milivolt')
    plt.plot(a, b)

    # EEG
    plt.subplot(2, 3, 2)
    plt.title("EEG")
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.plot(c, d)
    # EMG
    plt.subplot(2, 3, 3)
    plt.title("EMG")
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.plot(e, f)
def Spplot (a,b,c,):
    plt.subplot(2, 3, 4)
    powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(a)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    # EEG
    plt.subplot(2, 3, 5)
    powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(b)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    # EMG
    plt.subplot(2, 3, 6)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(c)

Signalplot(x1,y1,x2,y2,x3,y3)
Spplot(y1,y2,y3)
fig.tight_layout()
plt.savefig('Report.pdf')
