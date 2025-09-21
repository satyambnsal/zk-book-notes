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


# Addendum: Plonk vs Groth16 for Circom

We write the same circuit for both Plonk prover systems and the Groth16 prover system.

Groth16 allows an unlimited number of addition operations per constraint but only one non-constant multiplication. In contract, Plonk only allows one multiplication or one addition per constraint, and not both. The one-multiplication-per-constraint limitation will become apparent as we explore Circom.

However, Circom 




# References
https://calnix.gitbook.io/zk-notes/circom/8-circom-other-reference-circuits
