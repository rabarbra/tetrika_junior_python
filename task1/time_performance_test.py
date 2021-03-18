import timeit
import matplotlib.pyplot as plt
from task import task

x_ax = []
y_ax = []
n = 1
while n < 2 ** 10:
    t = float(timeit.timeit("task('0' * n)", "from __main__ import task, n"))
    x_ax.append(n)
    y_ax.append(t)
    print(n, t)
    n = n * 2

fig = plt.figure()
ax = fig.add_subplot()
ax.plot(x_ax, y_ax)
ax.set_xlabel("array length")
ax.set_ylabel("time(seconds)")
plt.savefig("performance.png")
plt.show()
