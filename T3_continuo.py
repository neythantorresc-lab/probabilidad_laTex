import sympy as sp

x, y = sp.symbols('x y')
f = 2

resultado = sp.integrate(sp.integrate(f, (x, 0, y)), (y, 0, 1))
print("Resultado:", resultado)
