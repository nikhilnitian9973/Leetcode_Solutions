class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans = strs[0];
        for (int i = 1;i<strs.size();i++){
            string curr_match;
        
            for (int j= 0;j<ans.size();j++){
                if (j== strs[i].size()) break;
                if (ans[j] != strs[i][j]) break;
                curr_match += ans[j];
            }
            ans = curr_match;


        }
        return ans;
    }
};