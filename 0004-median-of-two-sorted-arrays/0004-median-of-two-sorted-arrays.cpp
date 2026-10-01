class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int l = 0;
        int r = 0;
        int tot_size = nums1.size() + nums2.size();
        int lis[tot_size];
        int index = 0;
        int n = nums1.size(),m = nums2.size();
        while (l != n and r!= m){

            if (nums1[l] < nums2[r]){
                lis[index] = nums1[l];
                l +=1;
            }
            else{
                lis[index] = nums2[r];
                r+=1;
            }
            index +=1;
        }
        
        
        while (l != n){
            lis[index] = nums1[l];
            l+=1;
            index +=1;
        }
        

        
        while (r != m){
            lis[index] = nums2[r];
            r+=1;
            index +=1;
        }
        
        if (tot_size %2)
            return float(lis[tot_size/2]);
        else
            return (lis[tot_size/2-1] + lis[tot_size/2])/2.0;
    }
};