import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

# Lorenz system equations
def lorenz_system(state, t, sigma, rho, beta):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# Function to solve the Lorenz system
def solve_lorenz(sigma, rho, beta, initial_state, t_end, num_steps):
    t = np.linspace(0, t_end, num_steps)
    solution = odeint(lorenz_system, initial_state, t, args=(sigma, rho, beta))
    return t, solution

# Plot Lorenz 3D phase diagram
def plot_lorenz_3d_phase_diagram(sigma, rho, beta, initial_state, t_end, num_steps):
    t, solution = solve_lorenz(sigma, rho, beta, initial_state, t_end, num_steps)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(solution[:, 0], solution[:, 1], solution[:, 2], lw=2)
    ax.set_title('Lorenz 3D Phase Diagram')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# Parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
initial_state = [0.1, 0.0, 0.0]
t_end = 25
num_steps = 10000

# Plot the 3D phase diagram
plot_lorenz_3d_phase_diagram(sigma, rho, beta, initial_state, t_end, num_steps)
