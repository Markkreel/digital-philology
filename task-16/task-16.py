import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Create a figure object
fig = plt.figure()

# Add an axis to the figure canvas at [0,0,1,1]
ax = fig.add_axes([0, 0, 1, 1])

# Plot (x, y) on the axis and set labels and titles
ax.plot(x, y, label='y = x*2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Plot of y = x*2')

# Plot (x, z) on the same plot and draw the line in red
ax.plot(x, z, color='red', label='z = x**2')

# Show the legend
ax.legend()

# Display the plot
plt.show()
