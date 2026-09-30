/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdlib.h>
#include <string.h>
int* maxDepthAfterSplit(char* seq, int* returnSize) {
    int n = strlen(seq);
    int* ans = (int*)malloc(n*sizeof(int));
    int depth = 0;
        for (int i = 0; i<n;i++){
            if (seq[i] == '(') {
                depth +=1;
                ans[i] =depth%2;
            }
            else{
                ans[i] = depth%2;
                depth -=1;
            }
        }
    *returnSize = n;
    return ans;
}