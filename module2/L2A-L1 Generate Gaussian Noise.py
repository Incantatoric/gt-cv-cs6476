# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:43:49 2019


"""
import cv2
import matplotlib.pyplot as plt
from random import randn
import numpy as np

# Generate Gaussian noise
noise = np.random.randn([1, 1000]);
[n, x] = plt.hist(noise, np.linspace(-3, 3, 21));
#disp([x; n]);
plt.plot(x, n);

''' TODO: Try generating other kinds of random numbers.
%      How about a 2D grid of random Gaussian values?'''