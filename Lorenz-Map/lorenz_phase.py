import numpy as np
import matplotlib.pyplot as plt
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

# Plot Lorenz phase diagrams
def plot_lorenz_phase_diagrams(sigma, rho, beta, initial_state, t_end, num_steps):
    t, solution = solve_lorenz(sigma, rho, beta, initial_state, t_end, num_steps)

    # x-y phase diagram
    plt.figure(figsize=(12, 4))
    plt.subplot(131)
    plt.plot(solution[:, 0], solution[:, 1])
    plt.title('x-y Phase Diagram')
    plt.xlabel('x')
    plt.ylabel('y')

    # x-z phase diagram
    plt.subplot(132)
    plt.plot(solution[:, 0], solution[:, 2])
    plt.title('x-z Phase Diagram')
    plt.xlabel('x')
    plt.ylabel('z')

    # y-z phase diagram
    plt.subplot(133)
    plt.plot(solution[:, 1], solution[:, 2])
    plt.title('y-z Phase Diagram')
    plt.xlabel('y')
    plt.ylabel('z')

    plt.tight_layout()
    plt.show()

# Parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0
initial_state = [0.1, 0.0, 0.0]
t_end = 25
num_steps = 10000

# Plot phase diagrams
plot_lorenz_phase_diagrams(sigma, rho, beta, initial_state, t_end, num_steps)
