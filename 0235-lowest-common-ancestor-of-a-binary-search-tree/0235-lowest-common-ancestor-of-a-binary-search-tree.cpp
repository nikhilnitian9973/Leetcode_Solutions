/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        int mx = max(p->val,q->val);
        int mn = min(q->val,p->val);
        while (root){
            if (mx < root->val) root = root->left;
            else if  (mn > root->val) root = root-> right;
            else return root;
        }
        return root;
    }
};