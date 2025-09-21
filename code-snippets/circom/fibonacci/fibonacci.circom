pragma circom 2.1.6;

template Fibonacci(n) {
  var offset = n + 1;
  assert(n > 2);

  signal fib[offset];
  signal output out;

  fib[0] <== 0;
  fib[1] <== 1;

  for (var i = 2; i < offset; i++) {
    fib[i] <== fib[i-1] + fib[i-2];
  }

  out <== fib[n];
  log("out",out);
}

component main = Fibonacci(5);
