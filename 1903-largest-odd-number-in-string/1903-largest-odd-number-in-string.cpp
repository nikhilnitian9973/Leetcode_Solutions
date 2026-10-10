class Solution {
public:
    string largestOddNumber(string num) {
        string ans;
        int last_odd_index = -1;
        for (int i = 0;i<num.size();i++){
            if (int(num[i])%2 !=0) last_odd_index = i;
        }
        int starting_index = 0;
        for (int i = 0;i<num.size();i++){
            if (num[i] != '0') break;
            starting_index++;
        }
        for (int i = starting_index;i<last_odd_index+1;i++){
            ans += num[i];
        }
        return ans;
    }
};