import pandas as pn 
import matplotlib as mp 
import numpy as np  
from matplotlib import pyplot as plt 


T=20
Time=np.zeros(T)
GapY=np.zeros(T)
GapPi=np.zeros(T)
GapI=np.zeros(T)
GapR=np.zeros(T)
epsilon=np.zeros(T)

# Parameters
alpha=1
phi=0.25
thetaPi=0.5
thetaY=0.5
# Steady state & Targets
BarY=100
StarPi=2
rho=2

A = np.array([[1, 0, alpha], 
    [-phi, 1, 0],
    [-thetaY, -thetaPi, 1]])

B = np.array([[0, 0, 0], 
    [0, 1, 0],
    [0, 0, 0]])

C = np.array([[1, 0, 0], 
    [0, 1, 0],
    [0, 0, 0]])

invA = np.linalg.inv(A)
psi1=invA.dot(B)
psi2=invA.dot(C)

print("The matrix A=")
print(A)
print("\nThe psi1 matrix is")
print(psi1)


for x in range(T-1):
	Time[x+1]=x+1
	if ((x>= 3) and (x<=5)): 
		epsilon[x]=1
	else:
		epsilon[x]=0

	GapPi[x+1]=psi1[1][1]*GapPi[x]+psi2[1][0]*epsilon[x]
	GapY[x+1]=psi1[0][1]*GapPi[x]+psi2[0][0]*epsilon[x]
	GapR[x+1]=psi1[2][1]*GapPi[x]+psi2[2][0]*epsilon[x]


Y = GapY + BarY
Pi = GapPi + StarPi
r = GapR + rho
i = r + Pi

fig1=plt.figure(1)
ax1 = plt.subplot2grid((3, 2), (0, 0), colspan=2)
ax1.plot(Time, epsilon)
ax1.set_title('epsilon')
plt.xticks(Time)
ax2 = plt.subplot2grid((3, 2), (1, 0))
ax2.plot(Time, r, 'tab:orange')	
ax2.set_title('Real rate')
ax3 = plt.subplot2grid((3, 2), (1, 1))
ax3.plot(Time, Y, 'tab:green')
ax3.set_title('Production')
ax4 = plt.subplot2grid((3, 2), (2, 0))
ax4.plot(Time, Pi, 'tab:red')
ax4.set_title('Inflation')
ax5 = plt.subplot2grid((3, 2), (2, 1))
ax5.plot(Time, i, 'tab:red')
ax5.set_title('Nominal rate')
mp.pyplot.show()


