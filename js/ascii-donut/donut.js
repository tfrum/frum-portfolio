let A = 0;
let B = 0;
let i, j, k;
let z = new Array(1760);
let b = new Array(1760);

function main() {
  // screen and 3D array
  console.clear();
  setInterval(() => {
    // arrays
    for (let idx = 0; idx < 1760; idx++) {
      b[idx] = ' ';
      z[idx] = 0;
    }

    // Here we calculate out 3d positions. I've just refactored the
    // fairly famous donut.c code, and it's
    // more readable with lettered names than not.
    for (j = 0; j < 6.28; j += 0.07) {
      for (i = 0; i < 6.28; i += 0.02) {
        let c = Math.sin(i);
        let d = Math.cos(j);
        let e = Math.sin(A);
        let f = Math.sin(j);
        let g = Math.cos(A);
        let h = d + 2;
        let D = 1 / (c * h * e + f * g + 5);
        let l = Math.cos(i);
        let m = Math.cos(B);
        let n = Math.sin(B);
        let t = c * h * g - f * e;
        let x = Math.floor(40 + 30 * D * (l * h * m - t * n));
        let y = Math.floor(12 + 15 * D * (l * h * n + t * m));
        let o = Math.floor(x + 80 * y);
        let N = Math.floor(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n));

        // Check our bounds and set ASCII character
        if (y >= 0 && y < 22 && x >= 0 && x < 80 && D > z[o]) {
          z[o] = D;
          b[o] = ".,-~:;=!*#$@"[Math.max(N, 0)];
        }
      }
    }

    // ASCII.print()
    console.log("\x1b[H");
    let output = '';
    for (k = 0; k < 1760; k++) {
      output += (k % 80 ? b[k] : '\n');
    }
    console.log(output);

    // Update angles to spinny spin.
    A += 0.04;
    B += 0.02;
  }, 50);
}

main();
