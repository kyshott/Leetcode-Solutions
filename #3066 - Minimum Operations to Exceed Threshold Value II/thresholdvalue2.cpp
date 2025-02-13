class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        //Using constructor to create a min heap priority queue so smallest elements are first to access.
        //Another important thing to note is that this min heap is created to store long values...
        std::priority_queue<long, std::vector<long>, std::greater<long>> priorityq(nums.begin(), nums.end());

        long valuetoadd;
        int operations = 0;

        long smallest;
        long secondsmallest;

        while(priorityq.size() >= 2) {
            //If our smallest value is larger or equal to k, then all other values must be >= k
            if(priorityq.top() >= k) {
                break;
            }
            //Store the two smallest values in the priority queue
            smallest = priorityq.top();
            priorityq.pop();
            secondsmallest = priorityq.top();
            priorityq.pop();

            valuetoadd = (smallest * 2) + secondsmallest;
            priorityq.push(valuetoadd);
            operations++;
        }
        return operations;
    }
};
