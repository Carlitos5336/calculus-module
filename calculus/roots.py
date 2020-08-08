import pandas as pd
import calculus.base as calc

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
