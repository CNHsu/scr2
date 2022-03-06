from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')


fig = plt.figure()
ax1 = fig.add_subplot (111,projection='3d')

x,y,z = np.loadtxt('test3d.txt', delimiter=',',unpack=True)
x2,y2,z2 = np.loadtxt('test3d2.txt', delimiter=',',unpack=True)
print(x,y,z)
ax1.plot_wireframe(x,y,z)
ax1.scatter(x,y,z,c='g',marker='x')

dx =np.ones(10)
dy =np.ones(10)
dz = x
#ax1.bar3d(x2,y2,dx,dx,dy,dz)
ax1.plot_wireframe(x2,y2,z2, rstride=3,cstride=3,color='b')
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()