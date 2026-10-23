class Solution {
public:
    int sortPermutation(vector<int>& nums) {
        int res = -1;
        for (int i = 0;i<nums.size();i++){
            if (i != nums[i]){
                if (res ==-1){
                    res = nums[i];
                }
                res &= nums[i];
            }
        }
        if (res == -1) return 0;
        return res;
    }
};