#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 10:16:01 2019

@author: fred
"""

import numpy as np
tensao = np.random.randn(3)
np.savetxt('myfile.txt', tensao, fmt="%12.6G", delimiter=' ')    # save to file
tensao = np.genfromtxt('myfile.txt', unpack=True) # read from file
tensao
