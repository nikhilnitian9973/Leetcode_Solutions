class Solution {
public:
    int digit_sum(int);
    int smallestIndex(vector<int>& nums) {
        

        for (int i = 0; i< nums.size();i++){
            if (i == digit_sum(nums[i])){
                return i;
            }
        }
        return -1;

    }
};

int Solution::digit_sum(int num){
            int sum = 0;
            while (num){
                sum += num%10;
                num /=10;
            
            }
            return sum;
        }