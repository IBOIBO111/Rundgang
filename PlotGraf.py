import matplotlib.pyplot as plt
import numpy as npy

t=npy.arange(0.0,6.29,0.1)
y=5*npy.sin(t)
z=5*npy.cos(t)
plt.plot(t,y,'r+',t,z,'bo',linewidth=2)
plt.xlabel('Zeit [s]')
plt.ylabel('y(t)')
plt.title('Diagrammüberschrift')
plt.grid(True)
plt.show()

