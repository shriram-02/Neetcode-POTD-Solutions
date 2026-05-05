class LRUCache {
private:
    int cap;
    list<pair<int,int>> dll; // {key, value}
    unordered_map<int, list<pair<int,int>>::iterator> mp;

public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        if (mp.find(key) == mp.end()) return -1;

        auto it = mp[key];
        int val = it->second;

        dll.erase(it);
        dll.push_front({key, val});
        mp[key] = dll.begin();

        return val;
    }
    
    void put(int key, int value) {
        if (mp.find(key) != mp.end()) {
            dll.erase(mp[key]);
        } else if (dll.size() == cap) {
            auto last = dll.back();
            mp.erase(last.first);
            dll.pop_back();
        }

        dll.push_front({key, value});
        mp[key] = dll.begin();
    }
};