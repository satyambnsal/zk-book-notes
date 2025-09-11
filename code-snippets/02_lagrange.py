### Polynomial p(x) that crosses through the points
(1,4),(2,8), (3,2), (4,1)

"""
For set of n points, there is a unique lowest-degree polynomial of at most degree n-1 that interpolates them.
The polynomial of lowest degree that interpolates the points is sometimes called the Lagrange Polynomial

The consequence of this is that

if we use the points (1,2,..., n) as the x values to convert a length n vector to a polynomial via Lagrange Interpolation, then the resulting polynomial is unique.

In other words, given a consistent basis of x-values to interpolate a vector over, there is a unique polynomial that interpolates a given vector. Spoken another way, every length n vector has a unique polynomial representation.

Informally, every n degree vector has a unique n-1 degree polynomial that represent it. The degree could be less if, for example, the points are collinear, but the vector will be unique.


Q: What would be the value of  y points in this case ??
"""


from scipy.interpolate import lagrange
x_values = [1,2,3,4]
y_values = [4,8,2,1]

print(lagrange(x_values, y_values))

# import galois
# import numpy as np

# GF17 = galois.GF(17)

# xs = GF17(np.array([1,2,3,4]))
# ys = GF17(np.array([4,8,2,1]))

# p = galois.lagrange_poly(xs,ys)

# assert p(1) == GF17(4)
# assert p(2) == GF17(8)
# assert p(3) == GF17(2)
# assert p(4) == GF17(1)
