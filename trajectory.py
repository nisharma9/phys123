import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 1.0        # amplitude
alpha = 1.0    # angular frequency
t_vals = np.linspace(0.1, 10, 300)  # Avoid t=0 to prevent zero vectors

# Position function
x = A * alpha * t_vals * np.cos(alpha * t_vals)
y = A * alpha * t_vals * np.sin(alpha * t_vals)

# Velocity components (derivatives of x and y)
vx = A * alpha * (np.cos(alpha * t_vals) - alpha * t_vals * np.sin(alpha * t_vals))
vy = A * alpha * (np.sin(alpha * t_vals) + alpha * t_vals * np.cos(alpha * t_vals))

# Acceleration components (second derivatives)
ax = A * alpha * (-2 * alpha * np.sin(alpha * t_vals) - alpha**2 * t_vals * np.cos(alpha * t_vals))
ay = A * alpha * (2 * alpha * np.cos(alpha * t_vals) - alpha**2 * t_vals * np.sin(alpha * t_vals))

# Select a few points for vector visualization
sample_indices = np.linspace(0, len(t_vals) - 1, 20, dtype=int)

# Plotting
plt.figure(figsize=(10, 10))
plt.plot(x, y, label='Trajectory', color='blue')

# Plot velocity vectors (blue)
plt.quiver(x[sample_indices], y[sample_indices],
           vx[sample_indices], vy[sample_indices],
           color='blue', scale=30, label='Velocity')

# Plot acceleration vectors (orange)
plt.quiver(x[sample_indices], y[sample_indices],
           ax[sample_indices], ay[sample_indices],
           color='orange', scale=300, label='Acceleration')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectory of Particle with Velocity and Acceleration Vectors')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
