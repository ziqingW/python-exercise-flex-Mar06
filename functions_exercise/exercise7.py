import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plot

def f(x):
    return x * 1.8 + 32
    
xs = list(range(-100, 101))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.savefig('degree_conversion.png')
plot.close()