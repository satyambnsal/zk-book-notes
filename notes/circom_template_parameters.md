# Circom Template Parameters, Variables, Loops, If statements, Assert

With Circom, We're able to define a Rank 1 Constraint System(R1CS) using code instead of explicitly defining each constraint. 

```circom

template IsBinary() {
  signal input in[2];
  in[0] * (in[0] - 1) === 0;
  in[1] * (in[1] - 1) === 0;
}

component main = IsBinary();

```
Modify IsBinary to support **n** inputs

```circom
template IsBinary(n) {
  signal input in[n];

  for (var i =0; i < n; i++) {
    in[i] * (in[i] - 1) === 0;
  }
}

component main = IsBinary(4);
```
- **n** is known as a template parameter
- **n** is used within the circuit to specify the size of the array **in**
- on instantiating the template, we must specify the value of **n**

**Circuits and constraints in Circom must have a fixed, known structure**

Although constraints can be generated programmatically, the existence and configuration of constraints can not be conditionally depend on signals.

While templates can use parameters, the circuit must be static and clearly defined. There is no support for "dynamic-length" circuits or constraints - everything must be fixed and well defined from the start.

Imagine having an R1CS system of constraints whose structure was mutable based on input signal values. Neither the prover nor the verifier could operate as the number of constraints is not set in stone.

The value for **n** must be set at compile time.


**Variables:**

Variables hold non-signal data and are mutable. 
```
template VariableExample(n) {
  var acc = 2;
  signal s;
}
```
- By Default variables are not part of the R1CS system of constraints
  - Variables can be used as additive or multiplicative constants inside the R1CS.
  - Variables are used to compute values outside the R1CS to help define the R1CS.
  - When working with variables, Circom behaves like a normal programming language.
  - Math operations are done modulo **p**
    - '/' means multiplication with the multiplicative inverse, and '\' means integer division.
  - However, the only valid operators for signals are +, *, ===, <--, <==.

**If Statements**

Circom allows us to conditionally create constraints using if statements - but these conditions must be deterministic and known at compile time.

```
template EqualOnEven(n) {
  signal input in1[n];
  signal input in2[n];

  for (var i = 0; i < n; i++) {
    if (i % 2 == 0) {
      in1[i] === in2[i];
    }
  }
}

```

**Signals cannot be used for branching conditions in if statements or for loops**

The following code is not allowed because signal **a** is used as the conditional for the **if** statement.

```
template IfStatementViolation() {
  signal input a;
  signal input b;

  if (a == 2) {
    b === 3;
  } else {
    b === 4;
  }
}

```

In R1CS, there can only be addition and multiplication between signals. Circom is only a thin wrapper on top of R1CS. Therefore, it cannot "translate" an if statement to addition and multiplication.

### Using Variables as part of Constraints

Variables can be used as part of constraints. In the example, we enforce that the input array `in[n]` is a fibonacci sequence.

```
template IsFib(n) {
  assert(n > 1);
  signal input in[n];

  var correctFibo[n];
  correctFibo[0] = 0;
  correctFib[1] = 1;

  for (var i = 2; i < n; i++) {
    correctFibo[i] = correctFibo[i-1] + correctFibo[i-2];
  }

  for (var i = 0; i < n; i++) {
    in[i] === correctFibo[i];
  }

}
```
### Variables can be added to and Multiplied by other Signals
```
template IsIndexMultiplied(n) {
  signal input in1[n];
  signal input in2[n];

  for (var i =0; i < n; i++) {
    in1[i] * i === in2[i];
  }
}

component main = IsIndexMultiplied(3)
```

