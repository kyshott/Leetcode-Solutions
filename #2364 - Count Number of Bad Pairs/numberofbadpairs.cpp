#include <unordered_map> 

class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        long long total_pairs = (long long)nums.size() * (nums.size() - 1) / 2;
        long long good_pairs = 0;

        unordered_map<int, int> differences;
        
        for (int i = 0; i < nums.size(); i++) {
            int difference = nums[i] - i; // Calculate difference
            good_pairs += differences[difference]; // If this is the first difference, then add 0. If not, meaning the value is 1 - then add 1 to "good"... so on so forth...
            differences[difference]++; // Increment the number of "occurences" for that particular difference
        }
        
        return total_pairs - good_pairs;
    }
};
