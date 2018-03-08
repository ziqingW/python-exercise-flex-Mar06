import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plot
import math
from numpy import arange

def f(x):
    return math.sin(x)
    
xs = list(arange(-5, 6, 0.1))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.savefig('exercise6.png')
plot.close()