import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20,20,80)
y = np.sin(x)

plt.title("Hàm Sin")
plt.ylabel("Sin of x")
plt.xlabel("X value")
plt.grid(True)

plt.plot(x, y,linestyle = '--',color = 'r')
plt.show()