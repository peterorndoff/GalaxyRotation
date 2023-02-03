import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def initial_conditions(N, L):
    x = np.random.uniform(-L, L, N)
    y = np.random.uniform(-L, L, N)
    return x, y

def initial_velocities(x, y, v0):
    n = len(x)
    vx = np.zeros(n)
    vy = np.zeros(n)
    for i in range(n):
        r = np.sqrt(x[i]**2 + y[i]**2)
        vx[i] = -v0 * y[i] / (r+1e-10)
        vy[i] = v0 * x[i] / (r+1e-10)
    return vx, vy



def acceleration(x, y, M):
    G = 6.674e-11 # gravitational constant
    n = len(x) # number of stars
    ax = np.zeros(n) # x-component of acceleration
    ay = np.zeros(n) # y-component of acceleration
    for i in range(n):
        for j in range(i + 1, n):
            dx = x[j] - x[i]
            dy = y[j] - y[i]
            r = np.sqrt(dx**2 + dy**2)
            f = G * M[i] * M[j] / r**2
            ax[i] += f * dx / r
            ay[i] += f * dy / r
            ax[j] -= f * dx / r
            ay[j] -= f * dy / r
    return ax, ay


def simulate_galaxy(x, y, vx, vy, dt, steps):
    for i in range(steps):
        ax, ay = acceleration(x, y, M)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
    return x, y

def update(frame, x, y, vx, vy, dt, steps, scat):
    x, y = simulate_galaxy(x, y, vx, vy, dt, steps)
    scat.set_offsets(np.c_[x, y])
    return scat,


N = 10 # number of stars
M = 1 # masses of stars
x0 = np.random.uniform(-1, 1, N) # initial x positions of stars
y0 = np.random.uniform(-1, 1, N) # initial y positions of stars
vx0 = np.zeros(N) # initial x velocities of stars
vy0 = np.zeros(N) # initial y velocities of stars


steps = 1000
dt = 0.01
x, y = initial_conditions(N, 10)
vx, vy = initial_velocities(vx0, vy0, 100)

fig, ax = plt.subplots()
scat = ax.scatter(x, y)
ax.axis("equal")
ax.set_xlim(-2000, 2000)
ax.set_ylim(-2000, 2000)

ani = animation.FuncAnimation(fig, update, fargs=(x, y, vx, vy, dt, steps, scat), frames=1000, blit=True)
plt.show()