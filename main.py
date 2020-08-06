import calculus as calc

f = calc.Addition([calc.generate_Polynomial([1, 1, -1, 5]), calc.Sine(var='y'), calc.Logaritmic(base=2, var='z')])

print(f, f.evaluate({"x":2, "y":3.1416, "z":4}))