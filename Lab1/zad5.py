import math
n=int(input("Podaj n: "))
silnia=1
for i in range(1,n+1):
    silnia=silnia*i
print("Silnia z n=%d to %d" % (n,silnia))
