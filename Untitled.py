#!/usr/bin/env python
# coding: utf-8

# In[1]:
from pylab import *
# In[2]:
def H(w):
    wc = 4000*pi
    return 150 / (1.0 + 1j * w / wc)
# In[3]:
f = logspace(0.0,5) # frequencies from 10**0 to 10**5
# In[4]:
plot(f, 20*log10(abs(H(2*pi*f)))); xscale('log')
plt.xlabel ("Frecuencia (Hz)")
plt.ylabel ("Amplitud (dB)")
grid(color='k', linestyle='--', linewidth=1)

