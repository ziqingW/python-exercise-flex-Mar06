import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plot

def f(x):
    if x % 2 == 1:
        return 1
    else:
        return -1
    
xs = list(range(-5, 6))
ys = []
for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)
plot.savefig('exercise4.png')
plot.close()