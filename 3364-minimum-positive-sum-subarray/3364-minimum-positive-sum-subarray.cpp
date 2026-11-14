#include <algorithm>
class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int mini = INT_MAX;
        int sum = 0;
        int i = 0,j = 0;
        int n = nums.size();
        while (j<n){
            int len = j-i+1;
            sum += nums[j];
            if (len >r) {
                sum -= nums[i];
                i++;
            }
            int temp = sum;
            int k = i;
            while (j-k+1 >=l){
            if (temp >0) mini = mini<temp? mini:temp;
            temp -= nums[k];
            k++;

            }   
            

            
            
            j++;
        }
        return mini== INT_MAX ? -1:mini;
    }
};