1. Generate constraint


```
circom 01.circom --r1cs --wasm --sym --c
```
# Computing our witness with WebAssembly

```
node generate_witness.js <filename>.wasm input.json witness.wtns
```

# Proving circuits
Groth16 requires a per circuit trusted setup.
- The powers of tau, which is independent of the circuit
- The phase 2, which depends on the circuit.


## Powers of Tau
```
snarkjs powersoftau new bn128 12 port12_0000.ptau -v
```
Contribute to the ceremony
```
snarkjs powersoftau contribute port12_0000.ptau port12_0001.ptau --name="First contribution" -v
```

## Phase 2
```
snarkjs powersoftau prepare phase2 port12_0001.ptau pot12_fina.ptau -v
```

We generate a .zkey file that will contain the proving and verification keys together with all phase2 contributions.

```
snarkjs groth16 setup fibonacci.r1cs pot12_fina.ptau fibonacci_0000.zkey
```
Contribute to the phase 2 of ceremony
```
snarkjs zkey contribute fibonacci_0000.zkey fibonacci_0001.zkey --name="1st contribution" -v

Export verification key
```
snarkjs zkey export verificationkey multiplier2_0001.zkey verification_key.json
```

# Gnerate a proof
```
snarkjs groth16 prove fibonacci_0001.zkey witness.wtns proof.json public.json
```

# Veify a proof
```
snarkjs groth16 verify verification_key.json public.json proof.json
```

Export Witness as Json
```
snarkjs wtns export json fibonacci_js/witness.wtns witness.json
```
