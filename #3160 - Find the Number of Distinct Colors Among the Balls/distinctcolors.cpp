#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> queryResults(int limit, std::vector<std::vector<int>>& queries) {
        std::unordered_map<int, int> colorMap;
        std::unordered_map<int, int> colorFreq;
        std::vector<int> results;
        int distinctColors = 0;

        for(std::vector<int> query : queries) {
            int pos = query[0], newColor = query[1];

            if(colorMap.count(pos)) {
                int oldColor = colorMap[pos];
                
                colorFreq[oldColor] -= 1;

                //If the old color has a frequency of 0, then there are 0 of that color meaning
                //the number of unique colors for that query goes down
                if(colorFreq[oldColor] == 0) {
                    distinctColors -= 1;
                }
            }

            colorMap[pos] = newColor;

            //If the current color does not exist in the map or has a value of 0 then update
            //the frequency count, as a new color has come into play
            if(colorFreq[newColor] == 0) {
                distinctColors += 1;
            }
            colorFreq[newColor] += 1;

            results.push_back(distinctColors);
        }
        
        return results;
    }
};
