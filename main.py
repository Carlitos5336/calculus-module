import calculus.functions as calc
import calculus.num_methods as met

f = calc.Product([calc.generate_Polynomial([1, -5, -24]), calc.Sine()])

print(f)
print(met.simpson_method(f, [1, 3])['Result'])