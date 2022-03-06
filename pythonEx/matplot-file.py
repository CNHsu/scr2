import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('test.txt','r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
        
plt.plot(x,y,label='load from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title(' Graph\n Check file !')
plt.legend()
plt.show()
