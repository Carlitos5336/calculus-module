# Made by Carlos Ogando 04/08/20

import math
import numpy as np

def inside_format(inside, empty):

  if(inside != None):
    return '(' + str(inside) + ')'
  else:
    return empty

def coeff_format(coeff):
  if coeff == 1:
    return ""
  elif coeff == -1:
    return "-"
  else:
    return str(coeff)

def chain_rule(function, derivative, var='x'):
  if(function.inside == None):
    if function.var != var:
      return Product([derivative, ImplicitDerivative(function.var)])
    else:
      return derivative
  else:
    derivative.inside = function.inside
    return Product([derivative, function.inside.differentiate(var=var)])

def generate_Polynomial(coeffs, exps=None, var='x'):
  if(exps==None):
    exps = [i for i in range(len(coeffs) - 1, -1, -1)]
  funcs=[]
  for i in range(len(coeffs)):
    n_exp = exps[i]
    n_coeff = coeffs[i]
    funcs.append(Polynomial(exp=n_exp, coeff=n_coeff, var=var))
  return Addition(funcs)

def evaluate_inside(function, inps):
  try:
    if isinstance(inps, (int, float, complex)):
      inps = {'x':inps}
    val = inps[function.var]
    if(function.inside != None):
      val = function.inside.evaluate(inps)
    return val
  except:
    print("To evaluate must specify", function.var, "value")
    exit()

class ImplicitDerivative:

  def __init__(self, var):
    self.var = var

  def evaluate(self, inps=None):
    print("Cannot evaluate implicit derivative")
    exit()

  def differentiate(self, var=None):
    print("Cannot calculate derivative for an implicit derivative")
    exit()

  def __str__(self):
    return self.var + "'"

class Divission:

  def __init__(self, dividend, divisor, coeff=1):
    self.dividend = dividend
    self.divisor = divisor
    self.coeff = coeff

  def evaluate(self, inps):
    return self.dividend.evaluate(inps)/self.divisor.evaluate(inps) * self.coeff

  def differentiate(self, var='x'):
    divisor = Polynomial(exp=2, inside=self.divisor)
    prod1 = Product([self.dividend.differentiate(var=var), self.divisor])
    prod2 = Product([self.dividend, self.divisor.differentiate(var=var)], coeff =-1)
    dividend = Addition([prod1, prod2])
    return Divission(dividend, divisor)

  def __str__(self):
    div_str = '(' + str(self.dividend) + ')/(' + str(self.divisor) + ')'
    coeff_str = coeff_format(self.coeff)
    return coeff_str + div_str

class Addition:

  def __init__(self, funcs, coeff=1):
    new_funcs = []
    for func in funcs:
      if isinstance(func, Polynomial):
        if func.coeff==0:
          continue
      new_funcs.append(func)
    self.funcs = new_funcs
    self.coeff = coeff

  def evaluate(self, inps):
    total = 0
    for func in self.funcs:
      total += func.evaluate(inps)
    return total * self.coeff

  def differentiate(self, var='x'):
    new_funcs = []
    for func in self.funcs:
      new_funcs.append(func.differentiate(var=var))
    return Addition(new_funcs, coeff=self.coeff) 

  def __str__(self):
    add_str = ""
    for func in self.funcs:
      if func.coeff > 0 and add_str != "":
        add_str += '+'
      add_str += str(func)
    coeff_str = coeff_format(self.coeff)
    return coeff_str + add_str

class Product:

  def __init__(self, funcs, coeff=1):
    new_funcs = []
    for func in funcs:
      if isinstance(func, Polynomial):
        if func.exp==0 and func.coeff==1:
          continue
      new_funcs.append(func)
    self.funcs = new_funcs
    self.coeff = coeff

  def evaluate(self, inps):
    total = 1
    for func in self.funcs:
      total *= func.evaluate(inps)
    return total * self.coeff

  def differentiate(self, var='x'):
    parts = []
    for i in range(len(self.funcs)):
      factors = list(f for f in self.funcs)
      del factors[i]
      factors.append(self.funcs[i].differentiate(var=var))
      parts.append(Product(factors))
    prod = Addition(parts)
    return prod

  def __str__(self):
    prod_str = ""
    for func in self.funcs:
      if isinstance(func, (Addition, Divission)):
        prod_str += '(' + str(func) + ')*'
        continue
      elif isinstance(func, Polynomial):
        if func.exp != 0 and func.exp != 1:
          prod_str += '(' + str(func) + ')*'
          continue
      prod_str += str(func) + '*'
    prod_str = prod_str[0:len(prod_str)-1]
    coeff_str = coeff_format(self.coeff)

    return coeff_str + prod_str

class Polynomial:

  def __init__(self, coeff=1, exp=0, inside=None, var='x'):
    self.coeff = coeff
    self.exp = exp
    self.inside = inside
    self.var = var

  def evaluate(self, inps):
    val = evaluate_inside(self, inps)
    power = val**self.exp if val > 0 else -((-val)**self.exp)
    return self.coeff * power

  def differentiate(self, var='x'):
    new_exp = self.exp - 1
    new_coeff = self.coeff * self.exp
    derivative = Polynomial(coeff=new_coeff, exp=new_exp, var=self.var)
    return chain_rule(self, derivative, var=var)

  def __str__(self):
    empty_format = self.var
    inside_str = inside_format(self.inside, empty_format)
    coeff_str = str(self.coeff)
    if(self.exp != 0):
      coeff_str = coeff_format(self.coeff)
    exp_str = ""
    if(self.exp == 0):
      inside_str = ''
      exp_str = ""
    elif(self.exp != 1):
      exp_str = '^' + str(self.exp)
    return coeff_str + inside_str + exp_str

class Exponential:

  def __init__(self, coeff=1, base=math.e, inside=None, var='x'):
    self.coeff = coeff
    self.base = base
    self.inside = inside
    self.var = var

  def evaluate(self, inps):
    val = evaluate_inside(self, inps)
    return self.coeff * self.base**(val)

  def differentiate(self, var='x'):
    derivative = Exponential(coeff=self.coeff*math.log(self.base), base=self.base, var=self.var)
    return chain_rule(self, derivative, var=var)

  def __str__(self):
    empty_format = self.var
    inside_str = inside_format(self.inside, empty_format)
    coeff_str = coeff_format(self.coeff)
    base_str = "e^"
    if(self.base != math.e):
      base_str = str(self.base) + '^'
    return coeff_str + base_str + inside_str

class Logaritmic:

  def __init__(self, coeff=1, base=math.e, inside=None, var='x'):
    self.coeff = coeff
    self.base = base
    self.inside = inside
    self.var = var

  def evaluate(self, inps):
    val = evaluate_inside(self, inps)
    return self.coeff * math.log(val, self.base)

  def differentiate(self, var='x'):
    derivative = Polynomial(exp=-1, coeff=self.coeff/math.log(self.base), var=self.var)
    return chain_rule(self, derivative, var=var)

  def __str__(self):
    empty_format = '(' + self.var + ')'
    inside_str = inside_format(self.inside, empty_format)
    coeff_str = coeff_format(self.coeff)
    base_str = "ln"
    if(self.base != math.e):
      base_str = "log[" + str(self.base) + "]"
    return coeff_str + base_str + inside_str

class Sine:

  def __init__(self, coeff=1, inside=None, var='x'):
    self.coeff = coeff
    self.inside = inside
    self.var = var

  def evaluate(self, inps):
    val = evaluate_inside(self, inps)
    return math.sin(val)*self.coeff

  def differentiate(self, var='x'):
    derivative = Cosine(coeff=self.coeff, var=self.var)
    return chain_rule(self, derivative, var=var)

  def __str__(self):
    empty_format = '(' + self.var + ')'
    inside_str = inside_format(self.inside, empty_format)
    coeff_str = coeff_format(self.coeff)
    return coeff_str + "sin" + inside_str

class Cosine:

  def __init__(self, coeff=1, inside=None, var='x'):
    self.coeff = coeff
    self.inside = inside
    self.var = var

  def evaluate(self, inps):
    val = evaluate_inside(self, inps)
    return math.cos(val)*self.coeff

  def differentiate(self, var='x'):
    derivative = Sine(coeff = self.coeff*-1, var=self.var)
    return chain_rule(self, derivative, var=var)

  def __str__(self):
    empty_format = '(' + self.var + ')'
    inside_str = inside_format(self.inside, empty_format)
    coeff_str = coeff_format(self.coeff)
    return coeff_str + "cos" + inside_str