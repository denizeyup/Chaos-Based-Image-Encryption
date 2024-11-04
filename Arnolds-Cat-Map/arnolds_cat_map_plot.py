import matplotlib.pyplot as plt
import numpy as np

def arnold_cat_map(x, y, iterations):
    for _ in range(iterations):
        x, y = (2 * x + y) % 1, (x + y) % 1
    return x, y

x, y = np.meshgrid(np.linspace(0, 1, 512), np.linspace(0, 1, 512))

iterations = 50
x, y = arnold_cat_map(x, y, iterations)

plt.figure(figsize=(8, 8))
plt.scatter(x, y, s=1, c='black', marker='.')
plt.title("Arnold's Cat Map")
plt.show()
