import matplotlib.pyplot as plt
import numpy as np

def logistic_map(r, x):
    return r * x * (1 - x)

def bifurcation_diagram(rmin, rmax, rsteps, xsteps, x0):
    rs = []
    xs = []

    for r in np.linspace(rmin, rmax, rsteps):
        x = x0
        for i in range(xsteps):
            x = logistic_map(r, x)
            if i > xsteps / 2:
                rs.append(r)
                xs.append(x)

    plt.scatter(rs, xs, s=0.1)
    plt.xlabel('r')
    plt.ylabel('x')
    plt.title('Bifurcation Diagram for Logistic Map')
    plt.show()

# Adjust figure size by adding figsize parameter to increase resolution
plt.figure(figsize=(10, 6))

# Bifurcation diagram with color and style adjustments
bifurcation_diagram(2.4, 4.0, 10000, 1000, 0.5)
