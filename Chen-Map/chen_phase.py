import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def chen_system(t, y):
    a, b, c = 35, 3, 23
    x, y, z = y
    dx_dt = a * (y - x)
    dy_dt = (c - a) * x - x * z + c * y
    dz_dt = x * y - b * z
    return [dx_dt, dy_dt, dz_dt]

def solve_chen_system(a, b, c, initial_state, t_end, num_steps):
    t_span = [0, t_end]
    sol = solve_ivp(chen_system, t_span, initial_state, t_eval=np.linspace(0, t_end, num_steps))
    return sol.t, sol.y

# Solving Chen system
a, b, c = 35, 3, 23
initial_conditions = [1, 1, 1]
t_chen, sol_chen = solve_chen_system(a, b, c, initial_conditions, 100, 10000)

# x-y phase diagram
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.plot(sol_chen[0], sol_chen[1])
plt.title('x-y Phase Diagram')
plt.xlabel('x')
plt.ylabel('y')

# x-z phase diagram
plt.subplot(132)
plt.plot(sol_chen[0], sol_chen[2])
plt.title('x-z Phase Diagram')
plt.xlabel('x')
plt.ylabel('z')

# y-z phase diagram
plt.subplot(133)
plt.plot(sol_chen[1], sol_chen[2])
plt.title('y-z Phase Diagram')
plt.xlabel('y')
plt.ylabel('z')

plt.tight_layout()
plt.show()
