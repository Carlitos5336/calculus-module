# Made by Carlos Ogando 04/08/20

import math

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
    if isinstance(inps, int):
      inps = {'x':inps}
    val = inps[function.var]
    if(function.inside != None):
      val = function.inside.evaluate(inps)
    return val
  except:
    print("To evaluate must specify", function.var, "value")
    exit()

class Divission:

  def __init__(self, dividend, divisor):
    self.dividend = dividend
    self.divisor = divisor

  def evaluate(self, inps):
    return self.dividend.evaluate(inps)/self.divisor.evaluate(inps)

  def differentiate(self):
    divisor = Polynomial(exp=2, inside=self.divisor)
    dividend = Addition([Product([self.dividend.differentiate(), self.divisor]), Product([self.dividend, self.divisor.differentiate()])], signs = [1, -1])
    return Divission(dividend, divisor)

  def __str__(self):
    div_str = '(' + str(self.dividend) + ')/(' + str(self.divisor) + ')'
    return div_str

class Addition:

  def __init__(self, funcs, signs=None):
    self.funcs = funcs
    if(signs != None):
      self.signs = signs
    else:
      self.signs = list(1 for i in range(len(funcs)))

  def evaluate(self, inps):
    total = 0
    for i in range(len(self.funcs)):
      func = self.funcs[i]
      sign = self.signs[i]
      total += func.evaluate(inps) *  sign
    return total

  def differentiate(self):
    new_funcs = []
    for func in self.funcs:
      new_funcs.append(func.differentiate())
    return Addition(new_funcs, signs=self.signs) 

  def __str__(self):
    add_str = ""
    for i in range(len(self.funcs)):
      func = self.funcs[i]
      sign = self.signs[i]
      if(sign == 1 and i > 0):
        add_str += ' + '
      if(sign == -1):
        add_str += ' - '
      add_str += str(func)
    return add_str

class Product:

  def __init__(self, funcs):
    self.funcs = funcs

  def evaluate(self, inps):
    total = 1
    for func in self.funcs:
      total *= func.evaluate(inps)
    return total

  def differentiate(self):
    parts = []
    for i in range(len(self.funcs)):
      factors = list(f for f in self.funcs)
      del factors[i]
      factors.append(self.funcs[i].differentiate())
      parts.append(Product(factors))
    prod = Addition(parts)
    return prod

  def __str__(self):
    prod_str = ""
    for func in self.funcs:
      prod_str += '(' + str(func) + ')*'
    prod_str = prod_str[0:len(prod_str)-1]
    return prod_str

class Polynomial:

  def __init__(self, coeff=1, exp=0, inside=None, var='x'):
    self.coeff = coeff
    self.exp = exp
    self.inside = inside
    self.var = var

  def evaluate(self, inps):
    val = evaluate_inside(self, inps)
    return self.coeff * (val**self.exp)

  def differentiate(self):
    new_exp = self.exp - 1
    new_coeff = self.coeff * self.exp
    if(self.inside == None):
      return Polynomial(coeff=new_coeff, exp=new_exp)
    else:
      return Product([Polynomial(coeff=new_coeff, exp=new_exp, inside=self.inside), self.inside.differentiate()])

  def __str__(self):
    if(self.coeff == 0):
      return '0'
    inside_str = 'x'
    if(self.inside != None):
      inside_str = '(' + str(self.inside) + ')'
    exp_str = ""
    if(self.exp != 1):
      exp_str = '^' + str(self.exp)
    if(self.exp == 0):
      inside_str = ''
      exp_str = ""
    coeff_str = ""
    if(self.coeff != 1 or self.exp == 0):
      coeff_str = str(self.coeff)

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

  def differentiate(self):
    if(self.inside == None):
      return Exponential(coeff=self.coeff*math.log(self.base), base=self.base)
    else:
      return Product([Exponential(coeff=self.coeff*math.log(self.base), base=self.base, inside=self.inside), self.inside.differentiate()])

  def __str__(self):
    inside_str = 'x'
    if(self.inside != None):
      inside_str = '(' + str(self.inside) + ')'
    base_str = "e^"
    if(self.base != math.e):
      base_str = str(self.base) + '^'
    coeff_str = ""
    if(self.coeff != 1):
      coeff_str = str(self.coeff) + "*"
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

  def differentiate(self):
    if(self.inside == None):
      return Polynomial(exp=-1, coeff=1/math.log(self.base))
    else:
      return Product([Polynomial(exp=-1, coeff=1/math.log(self.base), inside=self.inside), self.inside.differentiate()])

  def __str__(self):
    inside_str = '(x)'
    if(self.inside != None):
      inside_str = '(' + str(self.inside) + ')'
    base_str = "ln"
    if(self.base != math.e):
      base_str = "log[" + str(self.base) + "]"
    coeff_str = ""
    if(self.coeff != 1):
      coeff_str = str(self.coeff) + "*"
    return coeff_str + base_str + inside_str

class Sine:

  def __init__(self, coeff=1, inside=None, var='x'):
    self.coeff = coeff
    self.inside = inside
    self.var = var

  def evaluate(self, inps):
    val = evaluate_inside(self, inps)
    return math.sin(val)*self.coeff

  def differentiate(self):
    if(self.inside == None):
      return Cosine()
    else:
      return Product([Cosine(inside=self.inside), self.inside.differentiate()])

  def __str__(self):
    inside_str = '(x)'
    if(self.inside != None):
      inside_str = '(' + str(self.inside) + ')'
    coeff_str = ""
    if(self.coeff != 1):
      coeff_str = str(self.coeff) + "*"
    return coeff_str + "sin" + inside_str

class Cosine:

  def __init__(self, coeff=1, inside=None, var='x'):
    self.coeff = coeff
    self.inside = inside
    self.var = var

  def evaluate(self, inps):
    val = evaluate_inside(self, inps)
    return math.cos(val)*self.coeff

  def differentiate(self):
    if(self.inside == None):
      return Sine(coeff = self.coeff*-1)
    else:
      return Product([Sine(inside=self.inside), self.inside.differentiate()])

  def __str__(self):
    inside_str = '(x)'
    if(self.inside != None):
      inside_str = '(' + str(self.inside) + ')'
    coeff_str = ""
    if(self.coeff != 1):
      coeff_str = str(self.coeff) + "*"
    return coeff_str + "cos" + inside_str