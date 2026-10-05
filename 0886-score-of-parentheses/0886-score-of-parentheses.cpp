class Solution {
public:
    int scoreOfParentheses(string s) {
        int depth = 0, ans = 0;

        for (int i = 0; s[i] != '\0';i++){
            if (s[i]== '(') depth++;
            else{
                depth--;
                if (s[i-1]=='(') ans += (1<<depth);

            }
        }
    return ans;
    }
};