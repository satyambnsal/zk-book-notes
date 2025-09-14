
# Quadratic Arithmetic Programs

A quadratic arithmetic program is an arithmetic circuit, specifically a R1CS represented as a set of polynomials. It is derived using Lagrange interpolation on a R1CS. unlike an R1CS, a Quadratic Arithmetic Program (QAP) can be tested for equality in O(1) time via the Schwartz-Zippel Lemma.


Because a Rank 1 Constraint System is entiredly composed of vector operations, we aim to test if

$$ L_a \circ R_a \overset{?}{=} O_a$$

holds in O(1) time instead of O(n) time (where n is the number of rows in L, R, and O)

## Homomorphism between vector addition and polynomial addition

**Vector addition is homomorphic to polynomial addition**

If we take two vectors, interpolate them with polynomials, then add the polynomials together, we get the same polynomial as if we added the vectors together and then interpolated the sum vector.

Let $L(v)$ be the polynomial resulting from Lagrange interpolation on the vector v using (1,2,..., n) as the x values, where n is the length of v. 
$$
L(v+w) = L(v) + L(w)
$$

Example
Let $f_1(x) = x^2\space and \space f_2(x) = x^3 f_1$ interpolates (1,1), (2,4), (3,9) or the vector [1,4,9] and $f_2$ interpolates [1,8,27]

The sum of the vectors is [2,12,36] and its is clear that $x^3 + x^2$ interpolates that. Let 
$$ 
f_3(x) = f_1(x) + f_2(x) = x^3 + x^2\\
f_3(1) = 1 + 1 = 2\\
f_3(2) = 8 + 4 = 12\\
f_3(3) = 27 + 9 = 36\\
$$


$$
L(\lambda v) = \lambda L(v)
$$
**Scalar multiplication is really vector addition**

When we say "multiply a vector by 3" we are really saying "add the vector to itself three times". 

We can think of both vectors under element-wise addition (in a finite field) and polynomials under addition (also in a finite field) as groups.

The group of vectors under addition in a finite field is homomorphic to the group of polynomials under addition in a finite field

This is critial because vector equality testing takes O(n) time, but polynomial equality testing takes O(1) time.

Thereforem whereas testing R1CS equality took O(n) time, we can leverage this homomorphism to test the equality of R1CS in O(1) time.

This is what a Quadratic Arithmetic Program is.

## A Rank 1 Constraint System in Polynomials

Consider that matrix multiplication between a rectangular matrix and a vector can be written in terms of  vector addition and scalar multiplication.

For example, if we have a 3 X 4 matrix A and a 4 dimensional vector v, then we can write the matrix multiplication as 

$$

A.v = \begin{bmatrix}
  a_{11} & a_{12} & a_{13} & a_{14} \\
  a_{21} & a_{22} & a_{23} & a_{24} \\
  a_{31} & a_{32} & a_{33} & a_{34}
\end{bmatrix}
\begin{bmatrix}
  v_1 \\ v_2 \\ v_3 
  \\ v_4
\end{bmatrix}

$$

We typically think of the vector v "flipping" and doing an inner product with each of the rows

$$
A.v = \begin{bmatrix}
  a_{11}.v_1 & a_{12}.v_2 & a_{13}.v_3 & a_{14}.v_4 \\
  a_{21}.v_1 & a_{22}.v_2 & a_{23}.v_3 & a_{24}.v_4 \\
  a_{31}.v_1 & a_{32}.v_2 & a_{33}.v_3 & a_{34}.v_4
\end{bmatrix}
$$

However, we could instead think of splitting matrix a into a bunch of vectors as follows:

$$
A = \begin{bmatrix}
  a_{11} \\ a_{21} \\ a_{31}
\end{bmatrix}, 
\begin{bmatrix}
  a_{12} \\ a_{22} \\ a_{32}
\end{bmatrix},
\begin{bmatrix}
  a_{13} \\ a_{23} \\ a_{33}
\end{bmatrix},
\begin{bmatrix}
  a_{14} \\ a_{24} \\ a_{34}
\end{bmatrix}
$$

and multiplying each vector by a scalar from the vector v:

$$
A.v = \begin{bmatrix}
  a_{11} \\ a_{21} \\ a_{31}
\end{bmatrix}\bullet{v_1} +
\begin{bmatrix}
  a_{12} \\ a_{22} \\ a_{32}
\end{bmatrix}\bullet{v_2}
\begin{bmatrix}
  a_{13} \\ a_{23} \\ a_{33}
\end{bmatrix}\bullet{v_3}
\begin{bmatrix}
  a_{14} \\ a_{24} \\ a_{34}
\end{bmatrix}\bullet{v_4}
$$

We have expressed matrix multiplication between A and v purely in terms of vector addition and scalar multiplication.

Because we have established earlier that the group of vectors under addition in a finite field is homomorphic to the group of polynomials under addition in a finite field, we can express the computation above in terms of polynomials that represent the vectors.

## Succintly testing that $Av_1 = Bv_2$
Suppose we have matrix A and B such that
$$
\begin{align}
A = \begin{bmatrix}
  6 & 3 \\
  4 & 7
\end{bmatrix} \\
B = \begin{bmatrix}
  3 & 9 \\
  12 & 6
\end{bmatrix}  \\
and\space vectors \space v_1 and \space v_2 \\

v_1 = \begin{bmatrix}
2 \\ 4  
\end{bmatrix} \\
v_2 = \begin{bmatrix}
2 \\ 2  
\end{bmatrix}
\end{align}
$$

We want to test if $Av_1 = Bv_2$

Now we want to find the homomorphic equivalent of 

$$
\begin{bmatrix}
  6 \\ 4
\end{bmatrix} \bullet 2 + 
\begin{bmatrix}
  3 \\ 7
\end{bmatrix} \bullet 4 \stackrel{?}{=} 
\begin{bmatrix}
  3 \\ 12
\end{bmatrix} \bullet 2 + 
\begin{bmatrix}
  9 \\ 6
\end{bmatrix} \bullet 2
$$

[Example code](../code-snippets/05_succinct_test.py)

**The final assert statement is able to test is $Av_1 = Bv_2 doing a single comparison instead of n$**

### R1CS to QAP: Succintly testing that $L_a \cdot R_a = O_a$

Since we know how to test if $Av_1 = Bv_2$ succintly, we can also test if $L_a \cdot R_a = O_a$ 

The matrices have m columns, so lets break each of the matrices into m column vectors and interpolate them on (1,2,...,n) to produce m polynomials each.

Let $u_1(x), u_2(x),..., u_m(x)$ be the polynomials that interpolate the column vectors of L.
Let $v_1(x), v_2(x),..., v_m(x)$ be the polynomials that interpolate the column vectors of R.
Let $w_1(x), w_2(x),..., w_m(x)$ be the polynomials that interpolate the column vectors of O.

Without loss of generality, lets say we have 4 columns(m = 4) and three rows(n = 3)

$$
L_a = \begin{bmatrix}
  u_1(x) & u_2(x) & u_3(x) & u_4(x) 
\end{bmatrix} \begin{bmatrix}
  a_1 \\ a_2 \\ a_3 \\ a_4
\end{bmatrix} \\
= a_1u_1(x) + a_2u_2(x) + a_3u_3(x) + a_4u_4(x) \\
= \sum_{i=1}^{4} a_iu_i(x)

$$

Observe that the final result is a single polynomial with degree at most n-1(since there are n rows in L, $u_1(x), u_2(x),..., u_m(x)$ have degree at most n-1)

In the general case, $L_a$ can be written as 
$$
\sum_{i=1}^{m}a_iu_i(x)
$$

Using the same steps above, each matrix-witness product in the R1CS $L_a \circ R_a = O_a$ can be transformed as 
$$
L_a \to \sum_{i=1}^{m}a_iu_i(x) \\
R_a \to \sum_{i=1}^{m}a_iv_i(x) \\
O_a \to \sum_{i=1}^{m}a_iw_i(x)
$$

Since each of the sum terms produce a single polynomial. we can write them as:

$$
L_a \to \sum_{i=1}^{m}a_iu_i(x) = u(x) \\
R_a \to \sum_{i=1}^{m}a_iv_i(x) = v(x)\\
O_a \to \sum_{i=1}^{m}a_iw_i(x) = w(x)
$$

## Why interpolate all the columns ?

Because of the homomorphisms $L(v_1) + L(v_2) = L(v_1 + v_2)$ and $L(\lambda v) = \lambda L(v)$, if we compute u(x) as $L(L_a)$ we get the same result as applying Lagrange interpolation to the columns of L and then multiplying each of the polynomials by the respective element in a and summing the result

$$
\sum_{i=1}^{m} a_i u_i(x) \; L(a) 
\;\big|\; \text{where } u_i(x) \text{ is the Lagrange interpolation of column } i \text{ of } L
$$

So why not just compute a single Lagrange interpolation instead of m ?

All parties involved need to have a common agreement on the QAP - the polynomial interpolations of the matrices before any proofs and verifications are done.

## Polynomial degree imbalance
However, we can't simply express the final result as 
$u(x)v(x) = w(x)$ because the degrees won't match. 

Multiplying two polynimials together result in a product polynomial whose degree is the sum of the degrees of the two polynomials being multiplied together.

Because each of the u(x), v(x), and w(x) will have degree n-1, u(x)v(x) will generally have degree 2n-2 and w(x) will have degree n-1, so they won't be equal even though the underlying vectors they multiplied are equal.

This is because the homomorphisms we established earlier only make claims about vector addition, not Hadamard product.

However, the vector that u(x)v(x) interpolates
$$
((1,u(1)v(1))),(2,u(2)v(2))...,(n, u(n)v(n))
$$
is the same as the vector w(x) interpolates
$$(1, w(1)), (2,w(2)),..., (n,w(n))$$

in other words
$$
((1,u(1)v(1))),(2,u(2)v(2))...,(n, u(n)v(n)) = (1, w(1)), (2,w(2)),..., (n,w(n))
$$

### Example of underlying equality

u(x) interpolates (1,2), (2,4), (3,8)
v(x) interpolates (1,4), (2,2), (2,8)

Hadamard product = [8,8,64]
If we multiply u(x) and v(x) together, we get w(x)
$$
w(x) = 4x^4 -18x^3 + 36x^2 -42x+28
$$

so we can make w(x) equal to u(x)v(x) if they interpolate the same y values over (1,2,...,n) ?

u(x)v(x) = w(x) + b(x)

and the equation will be balanced!

b(x) was simply computed as u(x)v(x) - w(x)

**Theorem**: if h(x) = f(x)g(x) and f(x) has set of roots ${r_f}$ and g(x) has set of roots {r_g}, then h(x) has roots ${r_f}\cup{r_g}$

