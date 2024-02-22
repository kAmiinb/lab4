import matplotlib.pyplot as plt
import numpy as np

N = 17

# Функція
def f(x):
  return np.sin(np.pi * x / N)

x = np.arange(0, 1, 0.01)
y = f(x)

# Побудова графіка
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

