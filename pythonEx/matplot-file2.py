import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

fig =plt.figure()

x,y = np.loadtxt('test.txt', delimiter=',',unpack=True)
x2,y2=np.loadtxt('test2.txt', delimiter=',',unpack=True)

ax1 = plt.subplot2grid((1,1), (0,0))
ax1.grid(True)
ax1.text(x2[3],y2[3],'example')
ax1.annotate('Good!',(x[5],y[5]),xytext=(0.2,0.9),
             textcoords='axes fraction',
             arrowprops=dict(facecolor='grey'))
#style.use('dark_background')
#plt.plot(x,y,label='load from file')
plt.bar(x,y,label='load from file',color='g')
plt.plot(x2,y2,label='load from file2',color='r')
plt.hist(y2,x2,label='hist',histtype='bar',rwidth=0.8)
plt.scatter(x,y,label='skitscat',color='k',s=25,marker="o")

plt.xlabel('x')
plt.ylabel('y')
plt.title(' Graph\n Check file !')
style.use('dark_background')
plt.legend()

plt.show()
