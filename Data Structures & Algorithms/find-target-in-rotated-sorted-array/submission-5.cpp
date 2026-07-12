class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;

        int i = -1;
        if (nums[l] > nums[r]) {
            // Find the intersection between sections
            int mid;
            while (l <= r) {
                mid = (l + r) / 2;
                if (nums[mid] > nums[mid + 1]) {
                    i = mid;
                    break;
                }
                if (nums[mid] > nums[l]) {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
        }
        int newl, newr;
        if (i == -1) {
            newl = 0;
            newr = nums.size() - 1;
        } else if (target >= nums[0]) {
            newl = 0;
            newr = i;
        } else {
            newl = i + 1;
            newr = nums.size() - 1;
        }

        int newMid;
        // Implement a binary search
        while (newl <= newr) {
            newMid = (newl + newr) / 2;
            if (nums[newMid] == target) {
                return newMid;
                break;
            }
            if (nums[newMid] < target) {
                newl = newMid + 1;
            } else {
                newr = newMid - 1;
            }
        }
        return -1;
    }
};
