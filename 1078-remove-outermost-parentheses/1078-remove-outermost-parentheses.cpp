class Solution {
public:
    string removeOuterParentheses(string s) {
        int n = s.size();
        int last_index = 0;
        
        int count = 0;
        
        string ans;
        for (int i = 0;i<n;i++){
            if (s[i] == '(') count++;
            if (s[i] == ')') count --;
            if (count == 0){
                for (int j = last_index +1; j<i;j++) {
                    ans += s[j];
                }
                last_index = i+1;
            }
        }
    return ans;
    }
};