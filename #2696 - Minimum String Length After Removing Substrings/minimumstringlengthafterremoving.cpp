#include <string>
#include <iostream>
#include <stack>

class Solution {
public:
    int minLength(string s) {

        stack<char> stack;
        stack.push(s[0]);

        for(int i = 1; i < s.length(); i++) {

            std::cout << stack.size() << std::endl;

            if(stack.size() > 0) {
            
                if((stack.top() == 'A' && s[i] == 'B') || (stack.top() == 'C' && s[i] == 'D')) {
                    stack.pop();
                    continue;
                }
            }
                stack.push(s[i]);
        }

        return stack.size();
    }
};
