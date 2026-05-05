class Twitter {
private:
    int time;
    unordered_map<int, unordered_set<int>> follows;
    unordered_map<int, vector<pair<int,int>>> tweets; // {time, tweetId}

public:
    Twitter() {
        time = 0;
    }
    
    void postTweet(int userId, int tweetId) {
        tweets[userId].push_back({time++, tweetId});
    }
    
    vector<int> getNewsFeed(int userId) {
        priority_queue<pair<int,int>> pq; // {time, tweetId}

        // include self
        follows[userId].insert(userId);

        for (int user : follows[userId]) {
            auto& t = tweets[user];
            for (int i = t.size() - 1; i >= 0 && i >= (int)t.size() - 10; i--) {
                pq.push(t[i]);
            }
        }

        vector<int> result;
        while (!pq.empty() && result.size() < 10) {
            result.push_back(pq.top().second);
            pq.pop();
        }

        return result;
    }
    
    void follow(int followerId, int followeeId) {
        if (followerId != followeeId)
            follows[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        if (followerId != followeeId)
            follows[followerId].erase(followeeId);
    }
};