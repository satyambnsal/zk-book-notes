pragma circom 2.0.0;

template XOR() {
  signal input a;
  signal input b;
  signal output out;

  out <== a + b - 2 * a * b;
  log("output", out);
}

// component main = XOR();

template IsBinary(n) {
  signal input in[n];

  for (var i =0; i < n; i++) {
    in[i] * (in[i] - 1) === 0;
  }
}

template IsIndexMultiplied(n) {
  signal input in1[n];
  signal input in2[n];

  for (var i = 0; i < n; i++) {
    in1[i] * i === in2[i];
  }
}

template QuadraticViolation1() {
  signal input a;
  signal input b;
  signal input c;
  signal input d;

  a * b === c * d;
}
// component main = IsBinary(4);

// component main = IsIndexMultiplied(4);

component main = QuadraticViolation1();
