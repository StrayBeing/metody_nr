import cmath
a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))
delta=cmath.sqrt(b**2-4*a*c)
print("Pierwiastki równania to x1={0} x2={1}".format((-b + delta) / (2*a), (-b - delta) / (2*a)))


