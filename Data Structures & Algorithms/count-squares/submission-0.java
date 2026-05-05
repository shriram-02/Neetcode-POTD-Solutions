class CountSquares {

    private java.util.Map<Integer, java.util.Map<Integer, Integer>> map;

    public CountSquares() {
        map = new java.util.HashMap<>();
    }
    
    public void add(int[] point) {
        int x = point[0], y = point[1];
        map.putIfAbsent(x, new java.util.HashMap<>());
        java.util.Map<Integer, Integer> yMap = map.get(x);
        yMap.put(y, yMap.getOrDefault(y, 0) + 1);
    }
    
    public int count(int[] point) {
        int x = point[0], y = point[1];
        if (!map.containsKey(x)) return 0;

        int result = 0;
        java.util.Map<Integer, Integer> yMap = map.get(x);

        for (int col : map.keySet()) {
            if (col == x) continue;

            int d = col - x;

            java.util.Map<Integer, Integer> colMap = map.get(col);

            int count1 = colMap.getOrDefault(y, 0);
            int count2 = yMap.getOrDefault(y + d, 0);
            int count3 = colMap.getOrDefault(y + d, 0);
            result += count1 * count2 * count3;

            count2 = yMap.getOrDefault(y - d, 0);
            count3 = colMap.getOrDefault(y - d, 0);
            result += count1 * count2 * count3;
        }

        return result;
    }
}