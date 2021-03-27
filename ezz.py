from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import csv
import time
import math
import matplotlib.figure as fg
flag=True
x=0


    def backword(self):
        plt.close()
        global x
        #print(x)
        x=x-10
        global flag
        flag =True
        data_set1= pd.read_csv('ecg1.csv')
        yb=data_set1.iloc[0:-1,1].values
        data_set1= pd.read_csv('ecg1.csv')
        xa=data_set1.iloc[2*int(((x-100)+abs(x-100))/2):2*x,0].values
        y1=data_set1.iloc[2*int(((x-100)+abs(x-100))/2):2*x,1].values
        plt.cla()
        axes = plt.gca()
        axes.set_ylim([min(yb),max(yb)])
        axes.plot(xa, y1, label='Channel 1')
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.show()

    def forword(self):
        plt.close()
        global x
        #print(x)
        x=x+10
        global flag
        flag =True
        data_set1= pd.read_csv('ecg1.csv')
        yb=data_set1.iloc[0:-1,1].values
        data_set1= pd.read_csv('ecg1.csv')
        xa=data_set1.iloc[2*int(((x-100)+abs(x-100))/2):2*x,0].values
        y1=data_set1.iloc[2*int(((x-100)+abs(x-100))/2):2*x,1].values
        plt.cla()
        axes = plt.gca()
        axes.set_ylim([min(yb),max(yb)])
        axes.plot(xa, y1, label='Channel 1')
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.show()

    def resume(self):
        plt.close()
        fig, ax = plt.subplots()
        global x
        #print(x)
        c=x
        global flag
        flag =True
        data_set1= pd.read_csv('ecg1.csv')
        yb=data_set1.iloc[0:-1,1].values
        def animate(i):
            global x
            global flag
            if not flag:
                self.ani.event_source.stop()
            else:
                x=i+c
                print(c,x)
                data_set1= pd.read_csv('ecg1.csv')
                xa=data_set1.iloc[2*int(((x-100)+abs(x-100))/2):2*x,0].values
                y1=data_set1.iloc[2*int(((x-100)+abs(x-100))/2):2*x,1].values
                plt.cla()
                axes = plt.gca()
                axes.set_ylim([min(yb),max(yb)])
                axes.plot(xa, y1, label='Channel 1')
                plt.legend(loc='upper left')
                plt.tight_layout()
        self.ani = FuncAnimation(plt.gcf(), animate, interval=0.001)
        plt.tight_layout()
        plt.show()


    def stop(self):
        global x
        print(x)
        global flag
        flag=False

    def start(self):
        plt.close()
        #fig, ax = plt.subplots()
        fig=fg()
        global x
        x=0
        global flag
        flag =True
        data_set1= pd.read_csv('ecg1.csv')
        yb=data_set1.iloc[0:-1,1].values
        def animate(i):
            global x
            global flag
            if not flag:
                self.ani.event_source.stop()
            else:
                x=i
                data_set1= pd.read_csv('ecg1.csv')
                xa=data_set1.iloc[2*int(((i-100)+abs(i-100))/2):2*i,0].values
                y1=data_set1.iloc[2*int(((i-100)+abs(i-100))/2):2*i,1].values
                #fig.cla()
                axes = fig.gca()
                axes.set_ylim([min(yb),max(yb)])
                axes.plot(xa, y1, label='Channel 1')
                #plt.legend(loc='upper left')
                #plt.tight_layout()
        self.ani = FuncAnimation(fig., animate, interval=0.001)
        plt.tight_layout()
        plt.show()