### What is Schwartz-Zippel Lemma

Nearly all ZK-Proof algorithms rely on the Schwartz-Zippel Lemma to achieve succintness.

The Schwartz-Zippel Lemma states that if we were given two polynomials p(x) and q(x) with degree $d_p$ and $d_q$ respectively, and if p(x) != q(x), then the number of points where p(x) and q(x) intersect is less than $max(d_p,d_q)$

![alt text](assets/image.png)
They intersect at two points, which is the maximum degree between the polynomials $y = x$ and $y = x^2$


The Schwartz-Zippel Lemma holds for polynomials in finite fields(all computations are done modulo a prime p)


**Polynomial equality testing**

We can test if two polynomials are equal by checking if all their coefficients are equal, but this takes O(d) time, where d is the degree of polynomial.

If instead we can evaluate the polynomials at a random point u and compare the evaluation in O(1) time.

That is, in a finite field $F_p$, we pick a random value u from $[0,p)$. Then we evaluate $y_f = f(u)$ and $y_g = g(u)$. If $y_f = y_g$, then one of the two things must be true:
1. f(x) = g(x)
2. f(x) != g(x) and we picked one of the d points where they intersect where $d=max(deg(f), deg(g))$

if d << p, then the situation 2 is unlikely to the point of being negligible


For example, if the fielfd $F_p$ has $p\approx2^254$(a little smaller than a uint256), and if the polynomials are not more than one million degree large, then the probability of picking a point where they intersect is 

$$\dfrac{1 * 10^6}{2^{254}}\approx \dfrac{2^{20}}{2^{254}} \approx \dfrac{1}{2^{234}} \approx \dfrac{1}{10^{70}}$$


To put a sense of scale on that, the number of atoms in the universe is about 10^78 to 10^82, so it is extremely unlikely that we will pick a point where the polynomials intersect, if the polynomials are not equal.


**Using the Schwartz-Zippel Lemma to test if two vectors are equal**


We can test if two vectors are equal in O(1) time by converting them to polynomial, then running the Schwartz- Zippel Lemma test on the polynomials. 

[See example](../code-snippets/01_zippel_lemma.py)


End goal is for prover to send a small string of data to the verifier that the verifier can quickly check.

Most of the time, a ZK proof is essentially a polynomial evaluated at a random point.

The difficulty we have to solve is that we don't if the polynomial is evaluated honestly. somehow we have to trust the prover isn't lying when they evaluate f(u).


How to represent an entire circuit as a small set of polynomials evaluated at a random point ??





