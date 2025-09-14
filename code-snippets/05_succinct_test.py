import galois
import numpy as np
import random


p = 17
GF = galois.GF(p)
u = random.randint(0,p)
tau = GF(u)


x_values = GF(np.array([1,2]))

def L(v):
  return galois.lagrange_poly(x_values, v)

p1 = L(GF(np.array([6,4])))
p2 = L(GF(np.array([3,7])))
q1 = L(GF(np.array([3,12])))
q2 = L(GF(np.array([9,6])))

print(p1)
print(p2)
print(q1)
print(q2)


lhs = p1(tau) * GF(2) + p2(tau) * GF(4)
rhs = q1(tau) * GF(2) + q2(tau) * GF(2)

assert lhs == rhs
