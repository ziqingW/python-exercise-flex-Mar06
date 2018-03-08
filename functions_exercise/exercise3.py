import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plot

def f(x):
    # put your code here
    return x ** 2
    
xs = list(range(-100, 101))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.savefig('exercise3.png')
plot.close()