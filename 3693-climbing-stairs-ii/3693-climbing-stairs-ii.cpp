class Solution {
public:
    int climbStairs(int n, vector<int>& costs) {
        vector <int> dp(n+1,INT_MAX);
        dp[0] = 0;
        for (int j = 1;j<n+1;j++){
            
            for (int i = max(0,j-3);i<j;i++){
                if (dp[i]== INT_MAX) continue;
                int mini_cost = dp[i] + costs[j-1] + (j-i)*(j-i);
                dp[j] = min(dp[j],mini_cost);

            }
        }
        return dp[n];
    }
};