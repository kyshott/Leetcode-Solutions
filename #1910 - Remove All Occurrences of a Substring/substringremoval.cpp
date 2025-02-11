class Solution {
public:
    string removeOccurrences(string s, string part) {

        std::string stack;

        for(char c : s) {
            stack.push_back(c);
            if(stack.size() >= part.size() && stack.substr(stack.size() - part.size()) == part) {
                stack.erase(stack.size() - part.size(), part.size());
            }
        }

        return stack;
    }
};
