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
    int df(TreeNode* node, bool is_left){
        if (node == nullptr) return 0;
        if (node->left == nullptr && node->right == nullptr){
            if (is_left) return node->val;
            else return 0;
        }
        return df(node->left,true) + df(node->right,false);
    }
    int sumOfLeftLeaves(TreeNode* root) {
        return df(root,false);
    }
};