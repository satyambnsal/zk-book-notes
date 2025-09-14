# Introduction to ZK Circuits with Circom

Circom is a programming language for creating Rank 1 Constraint Systems 

The R1CS format is of interest because of the utility of that format for constructing SNARKs, particularly Groth16. With SNARKs, we enable verifiable computation. When verifying, the interested party expends less computational effort to confirm the correctness than they would need to perform the computation themselves. It is also possible to generate the proof without revealing the underlying data, and in this case, we refer to it as zkSNARKs.


# Why Circom Exists
Circom was created to address two major issues in developing contraint systems for SNARKs

1. Manually designing contraint systems is tedious and error prone, especially when dealing with large scale or repetitive constraints.
2. Populating the witness is equally challenging and requires manual computation of intermediary values that could otherwise be derived programmatically.

Thus, Circom
1. Simplifies constraint design
2. automates witness population.


