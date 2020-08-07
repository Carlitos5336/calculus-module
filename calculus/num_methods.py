import pandas as pd
import calculus.functions as calc

def bisection_method(function, init_range, iterations=12):

  result = pd.DataFrame(columns=["Xi", "Xs", "Xa", "f(Xi)*f(Xa)", "Approximation", "Change"])

  xi = init_range[0]
  xs = init_range[1]
  xa = 0

  for it in range(iterations):

    xa = (xi+xs)/2
    fxi = function.evaluate(xi)
    fxa = function.evaluate(xa)

    result = result.append({"Xi":xi, "Xs":xs, "Xa":xa, "f(Xi)*f(Xa)":fxi*fxa, "Approximation":fxa, "Change":""}, ignore_index=True)

    if(fxa*fxi < 0):
      xs = xa
      result["Change"][it] = "xs = " + str(xa)
    elif(fxa*fxi > 0):
      xi = xa
      result["Change"][it] = "xi = " + str(xa)
    else: break

  print("Bisection Method")
  
  return result

def fixedPoint_method(functions, init_value, iterations=12):

  selected_function = None

  for func in functions:
    dfunc = func.differentiate()
    if(dfunc.evaluate(init_value) >= -1 and dfunc.evaluate(init_value) <= 1):
      print(func, " is a valid iterable function.")
      selected_function = func
    else:
      print(func, " is not a valid iterable function.")

  val = init_value

  result = pd.DataFrame(columns=['Root'])
  result = result.append({"Root":val}, ignore_index=True)

  for it in range(iterations):
    val = selected_function.evaluate(val)
    result = result.append({"Root":val}, ignore_index=True)

  print("Fixed Point Method")
  
  return result

def newtonRaphson_method(function, init_value, iterations=12):

  val = init_value
  dfunction = function.differentiate()

  result = pd.DataFrame(columns=['Root'])
  result = result.append({"Root":val}, ignore_index=True)

  for it in range(iterations):
    val -= function.evaluate(val)/dfunction.evaluate(val)
    result = result.append({"Root":val}, ignore_index=True)

  print("Newton-Raphson Method")
  
  return result

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