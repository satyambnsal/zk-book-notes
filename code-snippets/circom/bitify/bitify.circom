pragma circom 2.0.0;

// include "comparators.circom";
// include "aliascheck.circom";

template Num2Bits(n) {
  signal input in;
  signal output out[n];
  var lc1 = 0;

  var e2 = 1;

  for(var i =0; i < n; i++) {
    out[i] <-- (in >> i) & 1;
    out[i] * (out[i] - 1) === 0;
    lc1 += out[i] * e2;
    e2 = e2 + e2;
  }

  lc1 === in;
}

template Num2Bits_strict() {
  signal input in;
  signal output out[254];

  component aliasCheck = AliasCheck();
  component n2b = Num2Bits(254);
  in ==> n2b.in;

  for (var i = 0; i < 254; i++) {
    n2b.out[i] ==> out[i];
    n2b.out[i] ==> aliasCheck.in[i];
  }
}

template AliasCheck() {
  signal input in[254];

  component compConstant = CompConstant(-1);

  for (var i = 0; i < 254; i++) in[i] ==> compConstant.in[i];
  compConstant.out === 0; 
}

template CompConstant(ct) {
  signal input in[254];
  signal output out;

  signal parts[127];
  signal sout;

  var clsb;
  var cmsb;
  var slsb;
  var smsb;

  var b = (1 << 128) - 1;
  var a = 1;
  var e = 1;
  var i;

  for(i = 0; i < 127; i++) {
    var a = 1;
    var e = 1;
    var i;
  }
}

component main = Num2Bits(8);
