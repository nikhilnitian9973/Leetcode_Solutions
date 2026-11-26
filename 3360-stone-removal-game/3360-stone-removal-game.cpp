class Solution {
public:
    bool canAliceWin(int n) {
        int turn = 1;
        for (int i = 10;i>0;i--){
            if (turn && i>n) return false;
            if (!turn && i>n) return true;
            n = n-i;
            turn = (turn ==1)? 0:1;

        }
        
    return true;   
        
    }
};