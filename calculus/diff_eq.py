import pandas as pd
import calculus.base as calc
import math

def euler_method(equation, initial_cond, step, target, returnTable=True):

  table = pd.DataFrame(columns=['x', 'y', 'mx + b'])
  
  x = initial_cond[0]
  y = initial_cond[1]
  vars = {'x':x, 'y':y}
  result = 0

  iterations = math.ceil((target - x)/step)

  for i in range(iterations + 1):
    result = equation.evaluate(inps=vars)*step + y
    table = table.append({'x':x, 'y':y, 'mx + b':result}, ignore_index=True)
    y = result
    x += step
    vars = {'x':x, 'y':y}

  if returnTable:
    table = table.append({'x':"Result", 'y':result, 'mx + b':"-"}, ignore_index=True)
    return table
  else:
    return result
  