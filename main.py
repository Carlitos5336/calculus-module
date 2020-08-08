import calculus.base as calc
import calculus.roots as rt

g = calc.Polynomial(exp=1/3, inside=calc.generate_Polynomial([8, -1]))
print(rt.fixedPoint_method([g], -2))
