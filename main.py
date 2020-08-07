import calculus as calc

f = calc.Cosine(inside=calc.Addition([calc.Polynomial(exp=1, var='y'), calc.Exponential(inside=calc.Divission(calc.Polynomial(exp=1, var='z'), calc.Polynomial(exp=1)))]))

print(f)
print(f.differentiate(var='y'))