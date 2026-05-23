import matplotlib.pyplot as plt

import numpy as np

# Define y-values
y = np.linspace(0, 10, 100)

# Define two sets of x-values (representing your vertical lines)
x1 = np.sin(y) + 2
x2 = np.cos(y) + 4

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the vertical lines (optional, for visualization)
plt.plot(x1, y, label='Line 1')
plt.plot(x2, y, label='Line 2')

# Fill the area between the vertical lines
plt.fill_betweenx(y, x1, x2, color='lightblue', alpha=0.5, label='Filled Area')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Filling Area Between Vertical Lines')
plt.legend()
plt.grid(True)
plt.show()