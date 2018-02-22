# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 20:30:11 2018

@author: srinic
"""

import numpy
import time


startTime = time.time()

finalsum = numpy.sum(range(1000000000))

print('Total time elapsed: %d %f \n' % (finalsum, time.time() - startTime))
