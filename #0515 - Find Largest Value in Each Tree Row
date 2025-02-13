/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        std::vector<int> values;
        std::queue<TreeNode*> nodequeue;

        //In the case of empty tree
        if(root == NULL) {
            return values;
        }

        //Add the root to the queue to be processed first
        nodequeue.push(root);

        //Our current tree level; root will always be on level 0
        int level = 0;

        while(!nodequeue.empty()) {
            //The number of nodes in the level is equal to the current queue size...
            //This is how "deep" we need to go into the tree
            int levelcount = nodequeue.size();

            for(int i = 0; i < levelcount; i++) {
                TreeNode* currentNode = nodequeue.front();
                nodequeue.pop();

                if(i == 0) {
                    values.push_back(currentNode->val);
                }

                if(currentNode->val >= values[level]) {
                    values[level] = currentNode->val;
                }

                if(currentNode->left != nullptr) {
                    nodequeue.push(currentNode->left);
                }

                if(currentNode->right != nullptr) {
                    nodequeue.push(currentNode->right);
                }
            }
            level++;
        }
        return values;
    }
    
};
