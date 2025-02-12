#include <unordered_map>

class Solution {
public:
    int maximumSum(vector<int>& nums) {
        int sums[82];

        int final = -1;

        int currentSum;

        for(int i = 0; i < nums.size(); i++) {
            currentSum = digitSum(nums[i]);
            //If there is already a value at the digit sum index (If there is only 1, there cannot be a combination)
            if(sums[currentSum] != 0) {
                //Update answer if the current sum of (largest value of digit sum) + (current digit sum value) is larger
                final = std::max(final, nums[i] + sums[currentSum]);
            }
            //Store the current largest element for the digit sum index, use it for comparison later... Important!
            sums[currentSum] = std::max(sums[currentSum], nums[i]);
        }
        return final;
    }
    //Helper method for calculating digit sum... Could be more optimized by using % 9 maybe?
    int digitSum(int num) {
        int digitsum = 0;
        while(num > 0) {
            digitsum += num % 10;
            num = num / 10;
        }
        return digitsum;
    }
};
