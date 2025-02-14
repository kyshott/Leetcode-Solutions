class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        for(int i = 0; i < nums.size() - 1 ; i++){
            if(nums[i] == nums[i+1]) {
                return true;
            }
        }
        return false;
    }
};

/* A novel approach to the problem using a set, runs about the same time.
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::set<int> check;

        check.insert(nums.begin(), nums.end());

        if(check.size() == nums.size()) {
            return false;
        }
        else {
            return true;
        }
    }
};
*/
