class Solution {
public:
    vector<string> fizzBuzz(int n) {
        
        std::vector<string> vector;

        for(int i = 1; i <= n; i++) {
            if((i % 3 == 0) && (i % 5 == 0)) {
                vector.push_back("FizzBuzz");
            }
            else if(i % 3 == 0) {
                vector.push_back("Fizz");
            }
            else if(i % 5 == 0) {
                vector.push_back("Buzz");
            }
            else {
                vector.push_back(std::to_string(i));
            }
        }

        return vector;
    }
};
