import cvxpy  as cp
import numpy as np
import matplotlib.pyplot as plt
from line.funcs import *
from scipy.integrate import quad
import sys, os
sys.path.insert(0,'/home/root1/Downloads/CoordGeo')
#if using termux
import subprocess
import shlex
#Defining f(x)
def f(x,a,b,c,d):
        return a * x**3 + b * x**2 + c*x+d 
a = 1
b = -2
c = 1
d=0                       
label_str = "$4x^2 - 4x +4$"

#For minima using gradient ascent
cur_x = 2
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 3*a*x**2 + 2* b*x+c            



#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x -= alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

min_val = f(cur_x,a,b,c,d)
print("Minimum value of f(x) is ", min_val, "at","x =",cur_x)
plt.show()

#For maxima using gradient ascent
cur_x1 = 0.1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 3*a*x**2 + 2* b*x+c            



#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x1 = cur_x1            
    cur_x1 += alpha * df(prev_x1)   
    previous_step_size = abs(cur_x1 - prev_x1)   
    iters+=1  

min_val1 = f(cur_x1,a,b,c,d)
print("Maximum value of f(x) is ", min_val1, "at","x =",cur_x1)

x_cor1 = [2,2,0,0]
y_cor1 = [0,2,2,0]
plt.plot(x_cor1, y_cor1, 'r--')
x_cor1 = [0, 0]
y_cor1 = [-5, 5]
plt.plot(x_cor1, y_cor1, 'r')
x_cor1 = [-2, 3]
y_cor1 = [0, 0]
plt.plot(x_cor1, y_cor1, 'r')
#Plotting f(x)
x=np.linspace(-1,3,20)
y=f(x,a,b,c,d)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.1f},{min_val:.1f})')
plt.plot(cur_x1,min_val1,'o')
plt.text(cur_x1, min_val1,f'P({cur_x1:.1f},{min_val1:.1f})')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
#plt.savefig('/home/ramesh/fwc2022/python/10/codes/CoordGeo')
plt.show()
'''A = np.array(([2,0]))
B = np.array(([2,2]))
xAB = line_gen(B,A)
plt.plot(xAB[0,:],xAB[1,:])
#plt.plot(x_AB[0,:],x_AB[1,:],label='$Diameter$')'''

s=2*2
def integrand1(x):
    return x*(x-1)**2
A1,err=quad(integrand1, 0,2)
requiredarea=s-A1
print(requiredarea)

