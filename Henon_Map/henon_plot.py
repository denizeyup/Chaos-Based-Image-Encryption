import matplotlib.pyplot as plt

def henon_map(x, y, a=1.4, b=0.3):
    new_x = 1 - a * x**2 + y
    new_y = b * x
    return new_x, new_y

def generate_henon_map(x0, y0, iterations=10000):
    x_values = [x0]
    y_values = [y0]

    for _ in range(iterations):
        x, y = henon_map(x_values[-1], y_values[-1])
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

x0, y0 = 0, 0  # Initial coordinates
iterations = 10000

x_values, y_values = generate_henon_map(x0, y0, iterations)

plt.scatter(x_values, y_values, s=0.1)
plt.title('Henon Map')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
