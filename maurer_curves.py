import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-350, 350)
ax.set_ylim(-350, 350)
ax.set_aspect('equal')
ax.set_axis_off()

n = 5
d = 97

line1, = ax.plot([], [], color='blue', linewidth=0.5)
line2, = ax.plot([], [], color='red', linewidth=4)

def update(theta):
    k = theta * d * math.pi / 180
    r = 300 * math.sin(n * k)
    x = r * math.cos(k)
    y = r * math.sin(k)
    line1.set_data(np.append(line1.get_xdata(), x), np.append(line1.get_ydata(), y))
    
    k = theta * math.pi / 180
    r = 300 * math.sin(n * k)
    x = r * math.cos(k)
    y = r * math.sin(k)
    line2.set_data(np.append(line2.get_xdata(), x), np.append(line2.get_ydata(), y))

ani = animation.FuncAnimation(fig, update, frames=361, interval=10, repeat=False)

plt.show()
