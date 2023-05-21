//문제: 9466
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const TESTCASE = +input.shift();
  const BFS = (x, ARR) => {};
  for (let i = 0; i < TESTCASE; i++) {
    const [N, CONNECT_STR] = input.splice(0, 2);
    const CONNECT_ARR = CONNECT_STR.split(" ").map(Number);
    const visited = Array.from({ length: N }, (e) => (e = false));
    console.log(visited);
  }
}
