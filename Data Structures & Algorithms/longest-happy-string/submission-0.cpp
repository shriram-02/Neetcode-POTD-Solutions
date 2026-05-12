class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        priority_queue<pair<int, char>> pq;

        if (a > 0) pq.push({a, 'a'});
        if (b > 0) pq.push({b, 'b'});
        if (c > 0) pq.push({c, 'c'});

        string result;

        while (!pq.empty()) {
            auto [count1, ch1] = pq.top();
            pq.pop();

            int n = result.size();

            if (n >= 2 && result[n - 1] == ch1 && result[n - 2] == ch1) {
                if (pq.empty())
                    break;

                auto [count2, ch2] = pq.top();
                pq.pop();

                result += ch2;
                count2--;

                if (count2 > 0)
                    pq.push({count2, ch2});

                pq.push({count1, ch1});
            }
            else {
                result += ch1;
                count1--;

                if (count1 > 0)
                    pq.push({count1, ch1});
            }
        }

        return result;
    }
};