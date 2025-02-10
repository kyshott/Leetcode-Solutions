class Solution {
public:
    string clearDigits(string s) {
        for(int i = 0; i < s.length(); i++) {
            if(isdigit(s[i])) {
                s.erase(i, 1);
                if(i != 0) {
                    s.erase(i - 1, 1);
                }
                i = 0;
            }
        }
        return s;
    }
};
