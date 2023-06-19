"""
Definition of input forcing data

Author: Malte Müller (maltem@met.no)
Date: 01 June 2023

References:
[1] Zeng and Beljaars (2005), https://doi.org/10.1029/2005GL023030
"""

__author__ = "Malte Mueller"


import numpy as np
import matplotlib.pyplot as plt

class AtmosData:
    def  __init__(self):
        self.time = None
        self.snet = None
        self.lnet = None
        self.wspeed = None
