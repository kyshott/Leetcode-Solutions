#include <stack>
#include <algorithm>

/*
To be honest, this one is a little hacky with libraries but it works...
*/
class Solution {
public:
    int findDuplicate(vector<int>& nums) {

        std::vector<int> sortedNums = nums;
        std::sort(sortedNums.begin(), sortedNums.end());
        std::stack<int> numStack;

        numStack.push(sortedNums[0]);

        for(int i = 1; i < sortedNums.size(); i++) {
            if(sortedNums[i] == numStack.top()) {
                return sortedNums[i];
            }
            numStack.push(sortedNums[i]);
        }

        return 0;
    }
};
