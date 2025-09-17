import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Create a figure and an axis
fig, ax = plt.subplots()

# Generate initial data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a line object that will be updated during the animation
line, = ax.plot(x, y)

# Function to update the plot for each frame
def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))  # Shift the sine wave
    return line,

ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
