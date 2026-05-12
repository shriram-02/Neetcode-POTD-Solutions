class Solution {
public:
    string reorganizeString(string s) {
        unordered_map<char, int> freq;

        for (char c : s) {
            freq[c]++;
        }

        priority_queue<pair<int, char>> pq;

        for (auto& [ch, count] : freq) {
            pq.push({count, ch});
        }

        string result;

        pair<int, char> prev = {0, '#'};

        while (!pq.empty()) {
            auto [count, ch] = pq.top();
            pq.pop();

            result += ch;
            count--;

            if (prev.first > 0) {
                pq.push(prev);
            }

            prev = {count, ch};
        }

        if (result.size() != s.size())
            return "";

        return result;
    }
};