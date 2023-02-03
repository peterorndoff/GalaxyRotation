import matplotlib.pyplot as plt
import numpy as np
import time

# Set the number of stars in the simulation
n_stars = 100

# Set the initial positions and velocities of the stars
x = np.random.uniform(-2, 2, size=n_stars)
y = np.random.uniform(-2, 2, size=n_stars)
vx = np.random.uniform(-0.1, 0.1, size=n_stars)
vy = np.random.uniform(-0.1, 0.1, size=n_stars)

# Set the mass of the central black hole
mass_bh = 1e6

# Set the time step for the simulation
dt = 0.01

# Set the number of time steps for the simulation
n_steps = 100

# Set the softening length for the simulation
softening = 0.1

# Simulate the motion of the stars over time
for i in range(n_steps):
    # Calculate the gravitational acceleration from the central black hole
    r = np.sqrt(x ** 2 + y ** 2)
    ax = -x * mass_bh / (r ** 3 + softening ** 3)
    ay = -y * mass_bh / (r ** 3 + softening ** 3)

    # Update the velocity of the stars
    vx = vx + ax * dt
    vy = vy + ay * dt

    # Update the position of the stars
    x = x + vx * dt
    y = y + vy * dt

# Plot the final positions of the stars


for i in range(n_steps):
    # ...
    plt.clf()
    plt.scatter(x, y, s=100)
    plt.xlim(-10000, 10000)
    plt.ylim(-10000, 10000)
    plt.pause(0.001)
    time.sleep(0.01)
    plt.show()