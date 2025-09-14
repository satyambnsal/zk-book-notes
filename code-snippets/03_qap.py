import galois
import numpy as np

p = 17

GF = galois.GF(p)

xs = GF(np.array([1,2,3]))

v1 = GF(np.array([4,8,2]))
v2 = GF(np.array([1,6,12]))


def L(v):
  return galois.lagrange_poly(xs, v)

assert L(v1+v2) == L(v1) + L(v2)
