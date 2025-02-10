class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == target) {
                return i;
            }
            if(target > nums[i]) {
                if(i == nums.size() - 1) {
                    return i + 1;
                }
                else { 
                    continue;
                }
            }
            if(target < nums[i]) {
                if(i == 0) {
                    return 0;
                }
                else {
                    return i;
                }
            }
        }

        return 0;
    }
};
