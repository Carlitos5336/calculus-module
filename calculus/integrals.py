import pandas as pd
import calculus.base as calc

def middlePoint_method(function, interval, divs=6, returnTable=True):

  dx = (interval[1] - interval[0])/divs
  table = pd.DataFrame(columns=['Xi','(Xi + Xi+1)/2', 'F((Xi + Xi+1)/2)'])
  result = 0

  for i in range(divs + 1):
    xi = interval[0] + dx * i
    xhi = interval[0] + dx * (i + 0.5)
    fxhi = function.evaluate(xhi)
    if(i != divs):
      table = table.append({"Xi":xi, "(Xi + Xi+1)/2": xhi, 'F((Xi + Xi+1)/2)':fxhi}, ignore_index=True)
      result += fxhi * dx
    else:
      table = table.append({"Xi":xi, "(Xi + Xi+1)/2": "n/a", 'F((Xi + Xi+1)/2)':"n/a"}, ignore_index=True)
  
  if returnTable:
    return {'Result':result, 'Table':table}
  else:
    return result

def trapeze_method(function, interval, divs=6, returnTable=True):

  dx = (interval[1] - interval[0])/divs
  table = pd.DataFrame(columns=['Xi','F(Xi)', '(F(Xi) + F(Xi+1))/2'])
  result = 0

  for i in range(divs + 1):
    xi = interval[0] + dx * i
    xni = interval[0] + dx * (i + 1)
    fxi = function.evaluate(xi)
    fxni = function.evaluate(xni)
    sm = (fxi + fxni)/2
    if(i != divs):
      table = table.append({"Xi":xi, "F(Xi)": fxi, "(F(Xi) + F(Xi+1))/2":sm}, ignore_index=True)
      result += sm * dx
    else:
      table = table.append({"Xi":xi, "F(Xi)": fxi, '(F(Xi) + F(Xi+1))/2':"n/a"}, ignore_index=True)
  
  if returnTable:
    return {'Result':result, 'Table':table}
  else:
    return result

def simpson_method(function, interval, divs=6, returnTable=True):

  if(divs%2 != 0):
    print("To use Simpson's rule, number of divissions must be pair")
    return

  dx = (interval[1] - interval[0])/divs
  table = pd.DataFrame(columns=['Xi','F(Xi)'])
  result = 0

  for i in range(divs + 1):
    xi = interval[0] + dx * i
    fxi = function.evaluate(xi)
    table = table.append({"Xi":xi, "F(Xi)": fxi}, ignore_index=True)
    if(i == 0 or i == divs):
      result += fxi
    else:
      if i%2 == 0:
        result += 2*fxi
      else:
        result += 4*fxi
  
  result *= dx /3

  if returnTable:
    return {'Result':result, 'Table':table}
  else:
    return result