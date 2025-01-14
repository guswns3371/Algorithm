package 프로그래머스;

// https://school.programmers.co.kr/learn/courses/30/lessons/136798
public class 기사단원의_무기 {
    public static void main(String[] args) {
        System.out.println(solution(5, 3, 2));
        System.out.println(solution(10, 3, 2));
    }

    public static int solution(int number, int limit, int power) {
        int answer = 0;
        for (int i = 1; i <= number; i++) {
            answer += getNumOfDivisor(i, limit, power);
        }
        return answer;
    }

    private static int getNumOfDivisor(int num, int limit, int power) {
        int count = 0;
        for (int i = 1; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                if (num / i == i) {
                    count++;
                } else {
                    count += 2;
                }
            }

            if (count > limit) {return power;}
        }
        return count;
    }
}
