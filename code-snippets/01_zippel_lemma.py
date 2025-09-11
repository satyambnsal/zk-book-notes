import galois

import numpy as np

p = 103

GF = galois.GF(p)

xs = GF(np.array([1,2,3]))

v1 = GF(np.array([4,8,19]))
v2 = GF(np.array([4,8,19]))

def L(v):
  return galois.lagrange_poly(xs, v)

p1 = L(v1)
p2 = L(v2)

import random
u = random.randint(0,p)

lhs = p1(u)
rhs = p2(u)

assert lhs == rhs
