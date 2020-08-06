import calculus as calc

f = calc.Addition([calc.Polynomial(), calc.Sine()])

print(f.differentiate())