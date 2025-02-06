#include <stack>

class Solution {
public:
    bool isValid(string s) {

        std::stack<char> letterStack;

        for(int i = 0; i < s.length(); i++) {
            if(!letterStack.empty()) {
                if(letterStack.top() == '(' && s[i] == ')') {
                    letterStack.pop();
                    continue;
                }
                else if(letterStack.top() == '{' && s[i] == '}') {
                    letterStack.pop();
                    continue;
                }
                else if(letterStack.top() == '[' && s[i] == ']') {
                    letterStack.pop();
                    continue;
                }
            }
            letterStack.push(s[i]);
        }

        return(letterStack.empty());
    }
};
