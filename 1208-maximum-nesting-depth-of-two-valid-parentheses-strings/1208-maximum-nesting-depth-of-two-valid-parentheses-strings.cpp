class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int n = seq.size();
        vector <int> ans(n);
        int depth = 0;
        for (int i = 0; i<n;i++){
            if (seq[i] == '(') {
                depth +=1;
                ans[i] =depth%2;
            }
            else{
                ans[i] = depth%2;
                depth -=1;
            }
        }
        return ans;
    }
};