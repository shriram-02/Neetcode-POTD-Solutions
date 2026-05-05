class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        
        java.util.PriorityQueue<int[]> pq = new java.util.PriorityQueue<>(
            (a, b) -> a[0] - b[0]
        ); // {time, x, y}
        
        boolean[][] visited = new boolean[n][n];
        pq.offer(new int[]{grid[0][0], 0, 0});
        
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int time = cur[0], x = cur[1], y = cur[2];
            
            if (visited[x][y]) continue;
            visited[x][y] = true;
            
            if (x == n - 1 && y == n - 1) return time;
            
            for (int[] d : dirs) {
                int nx = x + d[0];
                int ny = y + d[1];
                
                if (nx >= 0 && ny >= 0 && nx < n && ny < n && !visited[nx][ny]) {
                    pq.offer(new int[]{
                        Math.max(time, grid[nx][ny]),
                        nx,
                        ny
                    });
                }
            }
        }
        
        return -1;
    }
}