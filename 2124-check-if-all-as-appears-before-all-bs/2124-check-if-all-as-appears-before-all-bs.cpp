class Solution {
public:
    bool checkString(string s) {
        bool past_b = false;
        for (int i= 0;i<s.size();i++){
            if (s[i]=='b') past_b = true;
            if (past_b && s[i]== 'a') return false;
        }
        return true;
    }
};