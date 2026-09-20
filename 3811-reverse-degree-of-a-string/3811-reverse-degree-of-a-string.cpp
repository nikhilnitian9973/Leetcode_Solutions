class Solution {
public:
    int reverseDegree(string s) {
        
        int sum = 0;
        int n = s.length();
        for (int i = 1;i<=n;i++){
            sum += i*(26-int(s[i-1])+97);

        }
        return sum;
    }
};