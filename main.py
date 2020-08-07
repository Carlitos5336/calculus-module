import calculus as calc

f = calc.Cosine(inside=calc.Addition([calc.Polynomial(exp=1, var='y'), calc.Polynomial(exp=1)]))

print(f.differentiate())