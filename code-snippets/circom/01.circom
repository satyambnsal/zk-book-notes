pragma circom 2.0.0;

template XOR() {
  signal input a;
  signal input b;
  signal output out;

  out <== a + b - 2 * a * b;
  log("output", out);
}

component main = XOR();
