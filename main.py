
import calculus.base as calc
import calculus.integrals as it

f = calc.Divission(calc.Logaritmic(), calc.Addition([calc.Polynomial(), calc.Exponential()]))

print(f)
print(f.differentiate())
print(it.middlePoint_method(f, [2, 6]))