import matplotlib.pyplot as plt

def logistic_map(r, x0, num_iterations):
    result = []
    x = x0
    for _ in range(num_iterations):
        result.append(x)
        x = r * x * (1 - x)
    return result

# Parameters
r_value = 3.8
initial_x = 0.2
iterations = 100

# Calculate logistic map data
logistic_data = logistic_map(r_value, initial_x, iterations)

# Plot the graph
plt.plot(logistic_data, marker='o', linestyle='-', color='b')
plt.title('Logistic Map')
plt.xlabel('Iteration')
plt.ylabel('Value')
plt.show()
