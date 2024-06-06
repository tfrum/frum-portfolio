class Donut {
    constructor(rotationSpeedA, rotationSpeedB) {
      this.A = 0;
      this.B = 0;
      this.rotationSpeedA = rotationSpeedA;
      this.rotationSpeedB = rotationSpeedB;
      this.z = new Array(1760).fill(0);
      this.b = new Array(1760).fill(' ');
    }
  
    render() {
      this.z.fill(0);
      this.b.fill(' ');
  
      for (let j = 0; j < 6.28; j += 0.07) {
        for (let i = 0; i < 6.28; i += 0.02) {
          let c = Math.sin(i);
          let d = Math.cos(j);
          let e = Math.sin(this.A);
          let f = Math.sin(j);
          let g = Math.cos(this.A);
          let h = d + 2;
          let D = 1 / (c * h * e + f * g + 5);
          let l = Math.cos(i);
          let m = Math.cos(this.B);
          let n = Math.sin(this.B);
          let t = c * h * g - f * e;
          let x = Math.floor(40 + 30 * D * (l * h * m - t * n));
          let y = Math.floor(12 + 15 * D * (l * h * n + t * m));
          let o = Math.floor(x + 80 * y);
          let N = Math.floor(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n));
  
          if (y >= 0 && y < 22 && x >= 0 && x < 80 && D > this.z[o]) {
            this.z[o] = D;
            this.b[o] = ".,-~:;=!*#$@"[Math.max(N, 0)];
          }
        }
      }
  
      this.A += this.rotationSpeedA;
      this.B += this.rotationSpeedB;
  
      return this.b;
    }
  }
  
class RenderingEngine {
    constructor() {
      this.donut1 = new Donut(0.04, 0.02);
      this.donut2 = new Donut(-0.04, -0.02);
    }
  
    start() {
      console.clear();
  
      setInterval(() => {
        console.clear();
        let output1 = this.donut1.render();
        let output2 = this.donut2.render();
        let combinedOutput = '';
        for (let k = 0; k < 1760; k++) {
          combinedOutput += (k % 80 ? (output1[k] !== ' ' ? output1[k] : output2[k]) : '\n');
        }
        console.log(combinedOutput);
      }, 50);
    }
}
  
let engine = new RenderingEngine();
engine.start();