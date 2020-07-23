# Example python in r
# https://www.youtube.com/watch?v=blAGLAhw6VE&t=56s
#setwd("E:/HOC PYTHON/Intro_Python")

a = 3
b = a*7

#-------
while b < 100:
  print(b)
  b = b*2
#------ 

import numpy as np
c = np.arange(15).reshape(3, 5)
c
c.shape
c.ndim
c.dtype.name
c.itemsize
c.size
type(c)

d = np.array([6,7,8])
d
type(d)
