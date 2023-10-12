import numpy as np
xp=0
xk=2*np.pi
krok=0.1
lp=np.abs((xk-xp)/krok)
lp_int=int(np.ceil(lp))
print("Liczba punktow wartosci x: %d" % lp)
x=xp
for i in range(0,lp_int):
	x=x+krok
	print("sin(%f)=%f" % (x,np.sin(x)))
