class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> sup;
        for (auto n : nums) {
            if (sup.contains(n)) {
                return true;
            }
            sup.insert(n);
        }
        return false;
    }
};