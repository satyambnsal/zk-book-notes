import numpy as np

import galois
from functools import reduce

GF = galois.GF(79)
a = GF(70)
b = GF(10)

print(a+b)

# 1, out, x, y, v1, v2, v3

L = np.array([
  [0,0,1,0,0,0,0],
  [0,0,0,0,1,0,0],
  [0,0,0,-5,0,0,0],
  [0,0,0,0,0,0,1]
])

R = np.array([
  [0,0,1,0,0,0,0],
  [0,0,0,0,1,0,0],
  [0,0,0,1,0,0,0],
  [0,0,0,0,1,0,0]
])

O = np.array([
  [0,0,0,0,1,0,0],
  [0,0,0,0,0,1,0],
  [0,0,0,0,0,0,1],
  [0,1,0,0,0,-1,0]
])

x = 4
y = -2
v1 = x * x
v2 = v1 * v1
v3 = -5 * y * y
z = v3 * v1 + v2

a = np.array([1,z,x,y, v1, v2, v3])

assert all(np.equal(np.matmul(L,a) * np.matmul(R,a), np.matmul(O,a))), "not equal"

L = (L+79) % 79
R = (R+79) % 79
O = (O+79) % 79

# print(L)
# print(R)
# print(O)

L_galois = GF(L)
R_galois = GF(R)
O_galois = GF(O)

x = GF(4)
y = GF(-2 + 79)
v1 = x * x
v2 = v1 * v1
v3 = GF(-5 + 79) * y * y
out = v3 * v1 + v2

witness = GF(np.array([1, out, x, y, v1, v2, v3]))

assert all(np.equal(np.matmul(L_galois, witness) * np.matmul(R_galois, witness), np.matmul(O_galois, witness))), "not equal"


def interpolate_column(col):
  xs = GF(np.array([1,2,3,4]))
  return galois.lagrange_poly(xs, col)


U_polys = np.apply_along_axis(interpolate_column, 0, L_galois)
V_polys = np.apply_along_axis(interpolate_column, 0, R_galois)
W_polys = np.apply_along_axis(interpolate_column, 0, O_galois)

print(U_polys[:2])
print(V_polys[:2])
print(W_polys[:1])

def inner_product_polynomials_with_witness(polys, witness):
  mul_ = lambda x, y: x * y
  sum_ = lambda x, y: x + y
  return reduce(sum_, map(mul_, polys, witness))

term_1 = inner_product_polynomials_with_witness(U_polys, witness)
term_2 = inner_product_polynomials_with_witness(V_polys, witness)
term_3 = inner_product_polynomials_with_witness(W_polys, witness)

print(term_1)

t = galois.Poly([1,78], field = GF) * galois.Poly([1,77], field = GF) * galois.Poly([1,76], field = GF) * galois.Poly([1,75], field=GF)

print(t)

h = (term_1 * term_2 - term_3) // t


print(h)

assert term_1 * term_2 == term_3 + h * t, "division has a remainder"

# The check executed above is very similar to what the verifier will check for


