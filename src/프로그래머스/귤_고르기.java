package 프로그래머스;

import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

// https://school.programmers.co.kr/learn/courses/30/lessons/138476?language=java
public class 귤_고르기 {
    public static void main(String[] args) {

        System.out.println(solution(6, new int[] { 1, 3, 2, 5, 4, 5, 2, 3 }));
        System.out.println(solution(4, new int[] { 1, 3, 2, 5, 4, 5, 2, 3 }));
        System.out.println(solution(2, new int[] { 1, 1, 1, 1, 2, 2, 2, 3 }));
    }

    public static int solution(int k, int[] tangerine) {
        int answer = 0;

        Map<Integer, Integer> map = new HashMap<>();
        for (int i : tangerine) {
            map.putIfAbsent(i, 0);
            map.put(i, map.get(i) + 1);
        }

        List<Integer> values = map.values().stream().sorted(Comparator.reverseOrder()).collect(Collectors.toList());
        for (Integer value : values) {
            k -= value;
            answer += 1;
            if (k <= 0) {break;}
        }

        return answer;
    }
}
