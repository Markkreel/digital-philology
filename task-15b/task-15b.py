'''
Inspired by https://github.com/PrateekKumarSingh/Python/tree/master/Python%20for%20Finance/Python-for-Finance-Repo-master/03-%20General%20Pandas/Pandas-Exercises

• Create a figure object called fig using plt.figure()
• Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax.
• Plot (x,y) on that axes and set the labels and titles.
• Plot (x,z) on the same plot and draw the line in red.

```
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
```
'''

import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()

# Add an axis to the figure canvas at [0,0,1,1]
axis = figure.add_axes([0, 0, 1, 1])

x = np.arange(0, 100)
y = x * 2
z = x ** 2

axis.plot(x, y, label='y = 2x')

axis.set_xlabel('x')
axis.set_ylabel('y')
axis.set_title('Plot of y = 2x')

axis.plot(x, z, color='red', label='z = x^2')

axis.legend()

plt.show()

