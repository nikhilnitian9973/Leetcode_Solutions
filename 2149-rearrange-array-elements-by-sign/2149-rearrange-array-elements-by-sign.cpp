class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        int pos =0,neg = 1;
        vector <int> ans(nums.size());
        for (int val: nums){
            if (val>0){
                ans[pos] = val;
                pos+=2;
            }
            else{
                ans[neg]=val;
                neg+=2;
            }
        }
        return ans;
    }
};