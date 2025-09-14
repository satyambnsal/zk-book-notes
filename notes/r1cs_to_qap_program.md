# R1Cs to QAP over a Finite Field in Python

To make the transformation from R1CS to QAP less abstract, lets use a real example

$$
z = x^4 - 5y^2x^2
$$
Converted to a Rank1 Constraint System, this becomes
$$
v_1 = xx \\
v_2 = v_1 * v_2 \\
v_3 = -5yy
-v2 + z = v3 * v1

The order of our prime field needs to equal to order of the elliptic curve.

But for now, we will pick a small number to make this managable. We will pick the prime number 79
