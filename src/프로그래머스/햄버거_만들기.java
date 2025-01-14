package 프로그래머스;

import java.util.LinkedList;
import java.util.stream.Collectors;

// https://school.programmers.co.kr/learn/courses/30/lessons/133502
public class 햄버거_만들기 {

    public static final String FORMAT = "%s %s%n";

    public static void main(String[] args) {
        System.out.printf(FORMAT, solution(new int[] { 2, 1, 1, 2, 3, 1, 2, 3, 1 }), 2);
        System.out.printf(FORMAT, solution(new int[] { 1, 3, 2, 1, 2, 1, 3, 1, 2 }), 0);
        System.out.printf(FORMAT, solution(new int[] { 1, 2, 3, 1, 2 }), 1);
        System.out.printf(FORMAT, solution(new int[] { 1, 2, 3, 1 }), 1);
        System.out.printf(FORMAT, solution(new int[] { 1, 2, 3, 1, 2, 3 }), 1);
        System.out.printf(FORMAT, solution(new int[] { 1, 1, 2, 3, 1, 2, 3, 1 }), 2);
        System.out.printf(FORMAT, solution(new int[] { 1, 1, 2, 3, 2, 3, 3, 1 }), 1);
    }

    public static int solution(int[] ingredient) {
        int answer = 0;
        String burger = "1231";
        LinkedList<Integer> stack = new LinkedList<>();
        for (int ing : ingredient) {
            stack.add(ing);
            if (ing == 1 && stack.size() >= 4) {
                String collect = stack.subList(stack.size() - 4, stack.size()).stream().map(String::valueOf).collect(Collectors.joining());

                if (burger.equals(collect)) {
                    answer++;
                    for (int i = 0; i < 4; i++) {
                        stack.pollLast();
                    }
                }
            }

        }

        return answer;
    }

    /**
     * sp 를 이용하여 현재 위치를 기억하는게 키 포인트
     */
    public static int solution2(int[] ingredient) {
        int[] stack = new int[ingredient.length];
        int sp = 0;
        int answer = 0;
        for (int i : ingredient) {
            stack[sp++] = i;
            if (sp >= 4 && stack[sp - 1] == 1
                && stack[sp - 2] == 3
                && stack[sp - 3] == 2
                && stack[sp - 4] == 1) {
                sp -= 4;
                answer++;
            }
        }
        return answer;
    }
}
