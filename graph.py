import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import final

# Data for plotting
data_set = final.by_name('Miami-Dade')
print(data_set)

t = []
s = []

for item in data_set:
    t += ''.join((data_set[data_set.index(item)][0][0:10]))
    print(data_set[data_set.index(item)][0])
    print(data_set.index(item))

    s += data_set[data_set.index(item)][5]
    print(data_set[data_set.index(item)][5])
   
    print(t)
    print(s)


fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()