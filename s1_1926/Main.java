package s1_1926;
/*
 * 그림 정보를 dfs로 찾으려면 상하좌우 1 찾아서 탐색 후에 스택에 저장 및 인출
 * 모두 끝나면 그림 넓이 계산, 그림 개수++ 값도 저장해야 함
 * 
 * <고민중...>
 * 1. 그림 정보들을 어떤 자료구조에 담을 것인지
 * -> 이차원 배열에 넣어서 좌표값 활용
 * 
 * 2. dfs 어떻게 만들것인지
 * -> 스택에 인접 좌표 넣고 방문한 좌표 저장할 배열필요, 방문하는 우선순위 방향 정해야함
 *    + visited = new boolean[n][m]
 *    
 * 3. 자바 문법을 어떻게 적용할 것인지
 * -> 배열 말고 링크드리스트 쓸거면 패키지 이용가능 +스택
 *    + 좌표 class 에다가 x, y값을 쌍으로 저장후 get 메소드까지 구현
 */
import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s= new Scanner(System.in);
		int row = s.nextInt(), col = s.nextInt();
		int map[][] = new int[row][col];
		for(int i = 0; i < row; i++) {
			for(int j = 0; j < col; j++) {
				map[i][j] = s.nextInt();
				System.out.printf("%d ", map[i][j]); }
			System.out.printf("\n");

		}
		
	}

}
