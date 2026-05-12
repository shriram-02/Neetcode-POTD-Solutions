class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> record;

        for (string op : operations) {
            if (op == "+") {
                int n = record.size();
                record.push_back(record[n - 1] + record[n - 2]);
            }
            else if (op == "D") {
                record.push_back(2 * record.back());
            }
            else if (op == "C") {
                record.pop_back();
            }
            else {
                record.push_back(stoi(op));
            }
        }

        int sum = 0;

        for (int score : record) {
            sum += score;
        }

        return sum;
    }
};