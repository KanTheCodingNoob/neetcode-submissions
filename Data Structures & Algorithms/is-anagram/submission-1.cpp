class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.size();
        int m = t.size();
        if (n != m) {
            return false;
        }
        std::array<int, 26> sOccurance{};
        std::array<int, 26> tOccurance{};

        for (char c : s) {
            sOccurance[c - 'a']++;
        }

        for (char c : t) {
            tOccurance[c - 'a']++;
        }

        return sOccurance == tOccurance;
    }
};
