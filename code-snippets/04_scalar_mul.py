import galois
import numpy as np

p = 17

GF = galois.GF(p)

xs = GF(np.array([1,2,3]))
v = GF(np.array([4,8,2]))

lambda_ = GF(15)

def L(v):
  return galois.lagrange_poly(xs,v)

assert L(lambda_ * v) == lambda_ * L(v)
