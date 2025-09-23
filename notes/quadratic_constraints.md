# Quadratic Constraints

### Circom Constraints

A Rank 1 Constraint System has at most one multiplication between signals per constraint. This is called a "quadratic" constraint. Any constraint containing an operation other than addition or multiplication will be rejected by Circom with the "Non quadratic constraints are not allowed" error.


**Constant multiplications do not count**

```
a * b === c
```

```
2a * 3b === 4c
```

```
ab + c === d
```

```
a + b + c === d
```

```
a * b + c === d + e + f
```



