class Solution {
public:
    int romanToInt(string s) {

        std::map<char,int> numerals;
        int total = 0;

        numerals['I'] = 1;
        numerals['V'] = 5;
        numerals['X'] = 10;
        numerals['L'] = 50;
        numerals['C'] = 100;
        numerals['D'] = 500;
        numerals['M'] = 1000;

        for (int i = 0; i < s.length(); i++) {
            if(numerals[s[i]] < numerals[s[i + 1]]) {
                total -= numerals[s[i]];
            }
            else {
                total += numerals[s[i]];
            }
        }
        return total;
    }
};
