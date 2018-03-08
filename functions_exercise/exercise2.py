import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plot

def f(x):
    # put your code here
    return x + 1
    
xs = list(range(-3, 4))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.savefig('exercise2.png')
plot.close()