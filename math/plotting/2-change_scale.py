#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# your code here]
plt.plot(x, y, '-b')
plt.xlabel("Time (years)")
plt.ylabel()
plt.title("Fraction Remaining")
plt.xlim(0, 28650)
plt.yscale('log')
plt.show()