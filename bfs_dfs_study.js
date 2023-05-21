// 1. table 탐색에 bfs, dfs 사용 코드
// visited array 생성 코드
let visited = Array.from({ length: ROW }, () => new Array(COLUMN).fill(false));

// 유효한 index인지 확인하는 함수
const isValidIndex = (row, col) => {
  return 0 <= row && row < ROW && 0 <= col && col <= COLUMN;
};

// 상하좌우 방향 담은 object
const directionObj = {
  up: [-1, 0],
  down: [1, 0],
  left: [0, -1],
  right: [0, 1],
};

// queue 를 사용한 BFS 코드
const BFS = (row, col) => {
  let queue = [[row, col]];

  while (queue.length !== 0) {
    let [x, y] = queue.shift();

    Object.values(directionObj).map((dir) => {
      let [nx, ny] = [x + dir[0], y + dir[1]];
      if (isValidIndex(nx, ny)) {
        if (MAP[nx][ny] === 1 && visited[nx][ny] === false) {
          visited[nx][ny] = true;
          queue.push([nx, ny]);
        }
      }
    });
  }
};

// 재귀를 사용한 DFS
const DFS = (row, col) => {
  Object.values(directionObj).map((dir) => {
    let [nx, ny] = [x + dir[0], y + dir[1]];

    if (isValidIndex(nx, ny)) {
      visited[NEW_ROW][NEW_COL] = 1;
      // 새로운 좌표가 마지막 행에 도달했다면 true
      if (NEW_ROW === M - 1) return true;
      // DFS를 계속 진행했을 경우 마지막에 true를 return하면
      // Back Tracking으로 결국 결과값은 true
      if (DFS(NEW_ROW, NEW_COL)) return true;
    }
  });
};
