import calculus as calc

f = calc.Addition([calc.Product([calc.Polynomial(exp=2), calc.Polynomial(var='y', exp=2)]), calc.Polynomial(var='z', exp=2)])

df = f.differentiate()

print(df)
print(df.differentiate())