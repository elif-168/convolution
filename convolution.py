# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:06:17 2022

@author: elifg
"""
# sinyaller ve sistemler ödevi
#Elif Gülerarslan
#21011007

#1. VE 2. SORU

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv


x=list()
y=list()


x_start=int(input("x sinyalinin başladığı indis:"))
x_stop=int(input("x sinyalinin bittiği indis:"))
x_zero=int(input("x sinyalinin kaçıncı elemanı 0'dadır:"))
n=int(input("x sinyalinin örnek sayısı:"))
for i in range(n):
    print(" x sinyalinin",(i+1),". elemanını giriniz")
    x.append(float(input()))
x=np.array(x)   
    

y_start=int(input("y sinyalinin başladığı indis:"))
y_stop=int(input("y sinyalinin bittiği indis:"))
y_zero=int(input("y sinyalinin kaçıncı elemanı 0'dadır:"))
m=int(input("y sinyalinin örnek sayısı:"))
for j in range(m):
    print(" y sinyalinin",(j+1),". elemanını giriniz")
    y.append(float(input()))
y=np.array(y);


x_time=np.linspace(x_start, x_stop, n);
y_time=np.linspace(y_start, y_stop, m);

plt.subplot(4,1,1);



plt.stem(x_time,x);
plt.xlabel("zaman")
plt.ylabel("değerler")
plt.title("x sinyali")

plt.subplot(4,1,2);


plt.stem(y_time,y);
plt.xlabel("zaman")
plt.ylabel("değerler")
plt.title("y sinyali")

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=1.2, wspace=0.4, hspace=1.25);


print("x sinyali:",x)
print("y sinyali:", y)


def myConv(x,n,y,m):
    con=list()
    i=0
    j=0 
    for i in range(m+n-1):
        sum=0
        for j in range(i+1):
            if (i-j)<n and j<m:
                sum=sum+(x[i-j]*y[j])
            
            
        con.append(sum)
    
    return con
    
    
convo=myConv(x,n,y,m)
convo=np.array(convo)


print("\nsıfırıncı indisteki eleman yıldızlarla belirtilmiştir\n")

print("myConv fonksiyonu:")

print("[",end='')
for i in range(m+n-1):
    if i==(x_zero+y_zero-2):
        print(" *",convo[i], "*  ",end='')
    else:
        print(convo[i], " ", end='')
print("]")
  

con_start=(-1)*(x_zero+y_zero-2)
con_stop=(m+n-1)-(x_zero+y_zero-1)

plt.subplot(4,1,3)

con_time=np.linspace(con_start, con_stop, m+n-1);

plt.stem(con_time, convo)

plt.xlabel("zaman")
plt.ylabel("değerler")
plt.title("myConv fonksiyonu ile konvolüsyon")


plt.subplot(4,1,4)

convo_py=np.convolve(x,y)


plt.stem(con_time, convo_py)

plt.xlabel("zaman")
plt.ylabel("değerler")
plt.title("numpy.convolve fonksiyonu ile konvolüsyon")



plt.show();


print("\nnumpy.convolve fonksiyonu:")


print("[",end='')

for i in range(m+n-1):
    if i==(x_zero+y_zero-2):
        print(" *",convo_py[i], "*  ",end='')
    else:
        print(convo_py[i], " ", end='')

print("]")

#3. SORU
freq=44100
time1=5
time2=10


x1 = sd.rec(int(time1 * freq), samplerate=freq, channels=2)

sd.wait()


x2 = sd.rec(int(time2 * freq), samplerate=freq, channels=2)

sd.wait()

write("x1.wav", freq, x1)
write("x2.wav", freq, x2)

