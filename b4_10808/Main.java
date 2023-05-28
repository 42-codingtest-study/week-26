package b4_10808;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		
		String str = s.next();
		HashMap<Character, Integer> map = new HashMap<>();

		for(char c = 'a'; c <= 'z'; c++) {

			map.put(c, 0);
		}
		for(char ch : str.toCharArray()) {
			if(map.containsKey(ch))
				map.put(ch, map.get(ch) + 1);

		}
		for(char ch : map.keySet()) {
			System.out.printf("%d ", map.get(ch));
			
		}
	}

}
   