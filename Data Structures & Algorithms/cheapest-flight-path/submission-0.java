class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int[] dist = new int[n];
        java.util.Arrays.fill(dist, Integer.MAX_VALUE);
        dist[src] = 0;

        for (int i = 0; i <= k; i++) {
            int[] temp = dist.clone();

            for (int[] f : flights) {
                int u = f[0], v = f[1], cost = f[2];
                if (dist[u] != Integer.MAX_VALUE && dist[u] + cost < temp[v]) {
                    temp[v] = dist[u] + cost;
                }
            }

            dist = temp;
        }

        return dist[dst] == Integer.MAX_VALUE ? -1 : dist[dst];
    }
}