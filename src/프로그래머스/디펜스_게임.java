package 프로그래머스;

import java.util.Collections;
import java.util.PriorityQueue;

// https://school.programmers.co.kr/learn/courses/30/lessons/142085
public class 디펜스_게임 {
    public static void main(String[] args) {
        System.out.println(solution(7, 3, new int[] { 4, 2, 4, 5, 3, 3, 1 }));
        System.out.println(solution(2, 4, new int[] { 3, 3, 3, 3 }));
        System.out.println(solution(10, 1, new int[] { 2, 2, 2, 2, 2, 10 }));
        System.out.println(solution(7, 3, new int[] { 5, 5, 5, 5, 2, 3, 1 }));
        System.out.println(solution(1, 6, new int[] { 2, 2, 2, 2, 3, 3, 1 }));
        System.out.println(solution(10, 1, new int[] { 2, 2, 2, 2, 10 }));
    }

    public static int solution(int n, int k, int[] enemy) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        for (int i = 0; i < enemy.length; i++) {
            int e = enemy[i];
            queue.add(e);
            n -= e;

            if (n < 0) {
                if (k <= 0) {return i;}
                k--;
                n += queue.poll();
            }
        }

        return enemy.length;
    }
}
