class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        for (int i = 1; i < n; i++) {
            int num = n - i;
            if ((to_string(i) + to_string(num)).find('0') == string::npos) {
                return {i, num};
            }
        }
        return {};
        
    }
};
