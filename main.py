import calculus.base as calc
import calculus.roots as rt
import pandas as pd

pd.options.mode.chained_assignment = None

f = calc.generate_Polynomial([1, 0, -8, 1])
df = f.differentiate()

print(df.evaluate(-1))
print(f)
print(f.differentiate())
print(rt.newtonRaphson_method(f, -3))