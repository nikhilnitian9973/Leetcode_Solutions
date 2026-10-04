class Solution {
public:
    bool checkValidString(string s) {
        int l = 0,h = 0;

        for (int i= 0; s[i]!= '\0'; i++){
            if (s[i] == '(') l +=1;
            else l-=1;

            if (s[i] != ')') h +=1;
            else h-=1;

            if (h<0) return false;
            l = max(l,0);
        
        }
    return (l == 0);
    }
};