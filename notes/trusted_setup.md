# Bilinear Pairings in Python, Solidity, and the EVM

Sometimes also called bilinear mappings, bilinear pairings allow us to take three numbers, a, b, and c where $ab = c$, and encrypt them to become $E(a), E(b), E(c)$, where E is an encryption function, then send the two encrypted values to a verifier who can verify $E(a)E(b) = E(c)$ but not know the original values. We can use bilinear pairings to prove that a 3r number is the product of the first two without knowing the first two original numbers.







**How it works ?**

When a scalar is multiplied by a point on an elliptic curve, another elliptic curve point is produced. that is $P = pG$ where p is scalar, and G is generator. given P and G we can not determine p.

Assume $pq = r$. what we are trying to do is take
```
P = pG
Q = qG
R = rG
```

and convince a verifier that the discrete logs of P and Q multiply to produce the discrete log of R.

if $pq=r, and\space P = pG, Q = qG, and\space R = rG$, then we want a function such that
$$f(P,Q) = R$$

an not equal to R when $pq != r$. This should be true of all combinations of p, q, and r in the group.

However, this is typically now how we express R when using bilinear pairings.

$$f(P,Q) = f(R, G)$$

G is the generator point, and can be thought of as 1. In this context. For example, pG means we did $(G + G+...+G)$ p times. G just means we took G and didn't add anything. So in a sense, this is the same as saying $P * Q = R * 1$

So our bilinear pairing is a function that if you plug in two elliptic curve points you get an output that corresponds to the product of the discrete logs of those two points.


$$ e(P1, P2) \eq$$

# Trusted Setup

Trusted Setup is a mechanism ZK-Snark uses to evaluate a polynomial at a secret value

$$f(x) = 3x^3 + 2x^2+ 5x+ 10$$
then the coefficients are [3,2,5,10] and we can compute the polynomial as 

$$f(x) = <[3,2,5,10], [x^3, x^2, x, 1]>$$

Now suppose that someone picks a secret scalar $\tau$ and computes $[\tau^3, \tau^2, \tau, 1]$

then multiplies each of those points with the generator points of a cryptographic elliptic curve group. The result would be as follows:

$[\Omega_3, \Omega_2, \Omega_1, G_1] = [\tau^3G_1, \tau^2G_1, \tau G_1, G_1]$

Now anyone can take the structure reference string(SRS)$[\Omega_3, \Omega_2, \Omega_1, G_1]$ and evaluate a degree 3 polynomial or less on $\tau$

For example, if we have degree 2 polynomial $g(x) = 4x^2 + 7x+ 8$, we can evaluate $g(\tau)$ by taking the inner product of the structured reference string with the polynomial:

$$<[0,4,7,8], [\Omega_3, \Omega_2, \Omega_1, G_1]> = 4\Omega_2 + 7\Omega_1 + 8G_1$$

We now have computed $g(\tau)$ without knowing what $\tau$ is!

This is also called a trusted setup because although we don't know what the discrete log of $g(\tau)$ is, the person who created the SRS does. This could lead to leaking information down the line, so we trust that the entity creating the trusted setup deletes $\tau$ and in no way remebers it!.



# Lagrange Interpolation with Python

Lagrange Interpolation is a technique for computing a polynomial that passes through a set of n points

Interpolating a vector as a polynomial

A straight line through two points

If we have two points, they can be interpolated with a line. For example, given (1, 1) and (2, 2), we can draw a line that intersects both points, it would be a degree 1 polynomial y = x.

The pattern that we can "draw a polynomial through" n points with a (at most) degree n-1 polynomial holds for any number of points. For example, the points (0,0), (1,1), (2,4) can be interpolated with $y = x^2$
