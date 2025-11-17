class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        
        int foundFlag = 0;
        int counter = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1 && foundFlag == 0) {
                foundFlag = 1;
                counter = 0;
            }
            else if (foundFlag == 1 && nums[i] == 1) {
                if (counter < k)
                    return false;
                else
                    counter = 0;
            }
            else {
                counter++;
            }
        }
        return true;
        
    }
};
