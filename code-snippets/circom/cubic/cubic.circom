pragma circom 2.0.0;
// x^3 + x + 5
template Cubic() {
  signal input x;
  signal input y;

  signal x_squared;
  signal x_cubed;

  x_squared <== x * x;
  x_cubed <== x_squared * x;

  y === x_cubed + x + 5;
}

component main = Cubic();

