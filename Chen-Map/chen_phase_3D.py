import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp

# Chen system equations
def chen_system(t, y):
    a, b, c = 35, 3, 23
    x, y, z = y
    dx_dt = a * (y - x)
    dy_dt = (c - a) * x - x * z + c * y
    dz_dt = x * y - b * z
    return [dx_dt, dy_dt, dz_dt]

# Function to solve the Chen system
def solve_chen_system(initial_state, t_end, num_steps):
    t_span = [0, t_end]
    sol = solve_ivp(chen_system, t_span, initial_state, t_eval=np.linspace(0, t_end, num_steps))
    return sol.t, sol.y

# Plot Chen 3D phase diagram
def plot_chen_3d_phase_diagram(initial_state, t_end, num_steps):
    t, solution = solve_chen_system(initial_state, t_end, num_steps)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(solution[1], solution[0], solution[2], lw=2)  # Plotting in the order of X, Y, Z
    ax.set_title('Chen 3D Phase Diagram')
    ax.set_xlabel('Y')
    ax.set_ylabel('X')
    ax.set_zlabel('Z')
    plt.show()

# Parameters
initial_state_chen = [1, 1, 1]
t_end_chen = 100
num_steps_chen = 10000

# Plot the 3D phase diagram
plot_chen_3d_phase_diagram(initial_state_chen, t_end_chen, num_steps_chen)
