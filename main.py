import calculus.base as calc
import calculus.diff_eq as de

f = calc.Addition([calc.Exponential(), calc.Polynomial(exp=1,var='y')])

print(de.euler_method(f, [0, 0], 0.01, 2)['Table'])
