class Solution {
public:
    int countPrimes(int n) {
        if (n<=2) return 0;
        // int s[n+1];
        // for (int i = 0;i<n+1;i++){
        //     s[i] = -1;
        // }
        
        int cnt = n-2;
        vector<int> s(n,1);
        for (int i = 2;i*i<n;i++){
            if (s[i]) {
                
                for (int j =i*i ; j<n;j+=i){
                    if (s[j]){
                        s[j] = 0;
                        cnt--;
                    }
                }

            }
        }
        return cnt;
        
    }
};