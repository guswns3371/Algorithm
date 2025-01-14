package 프로그래머스;

import java.util.Arrays;
import java.util.Comparator;

// https://school.programmers.co.kr/learn/courses/30/lessons/147354
public class 테이블_해시_함수 {
    public static void main(String[] args) {
        System.out.printf("%s %s", solution(new int[][] {
            new int[] { 2, 2, 6 }, new int[] { 1, 5, 10 }, new int[] { 4, 2, 9 }, new int[] { 3, 8, 3 }
        }, 2, 2, 3), 4);
    }

    public static int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        Arrays.sort(data, Comparator.comparingInt((int[] v) -> v[col - 1]).thenComparingInt(v -> -v[0]));
        for (int i = row_begin - 1; i <= row_end - 1; i++) {
            int temp = 0;
            for (int datum : data[i]) {
                temp += datum % (i + 1);
            }
            answer ^= temp;
        }

        return answer;
    }
}
