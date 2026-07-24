class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> nToIdx;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            nToIdx.insert({target - nums[i], i});
        }

        for (int i = 0; i < n; i++) {
            if (nToIdx.contains(nums[i]) && nToIdx[nums[i]] != i) {
                return {min(i, nToIdx[nums[i]]), max(i, nToIdx[nums[i]])};
            }
        }
        return {};
    }
};
