import java.util.ArrayDeque;

class Solution {
    private final int[] dx = { 0, 0, 1, -1 };
    private final int[] dy = { 1, -1, 0, 0 };
    private int xLen;
    private int yLen;

    public int solution(String[] board) {
        xLen = board.length;
        yLen = board[0].length();
        int[][] visited = new int[xLen][yLen];
        ArrayDeque<Vo> queue = new ArrayDeque<>();

        for (int i = 0; i < xLen; i++) {
            for (int j = 0; j < yLen; j++) {
                if (board[i].charAt(j) == 'R') {
                    queue.addLast(new Vo(0, i, j));
                    visited[i][j] = 1;
                    board[i] = board[i].replace('R', '.');
                }
            }
        }

        while (!queue.isEmpty()) {
            Vo vo = queue.removeFirst();
            int count = vo.count;
            for (int k = 0; k < 4; k++) {
                int xx = vo.x;
                int yy = vo.y;

                while (checkLocation(xx, yy) && board[xx].charAt(yy) != 'D') {
                    xx += dx[k];
                    yy += dy[k];
                }

                if (!checkLocation(xx, yy) || board[xx].charAt(yy) == 'D') {
                    xx -= dx[k];
                    yy -= dy[k];
                }

                if (checkLocation(xx, yy)) {
                    if (board[xx].charAt(yy) == 'G') {
                        return count + 1;
                    }
                    if (visited[xx][yy] != 1 && board[xx].charAt(yy) == '.') {
                        visited[xx][yy] = 1;
                        queue.addLast(new Vo(count + 1, xx, yy));
                    }
                }

            }
        }

        return -1;
    }

    private boolean checkLocation(int x, int y) {
        return (x >= 0 && x < xLen) && (y >= 0 && y < yLen);
    }

    class Vo {
        public Vo(int count, int x, int y) {
            this.count = count;
            this.x = x;
            this.y = y;
        }

        private int count;
        private int x;
        private int y;

    }
}
