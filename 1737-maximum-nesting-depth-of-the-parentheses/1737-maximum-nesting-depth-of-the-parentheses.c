int maxDepth(char* s) {
    int count= 0,maxi=0;
        for (int i = 0;s[i] != '\0';i++){
            if (s[i] == '(') count +=1;
            else if (s[i] == ')') count -=1;
            maxi = maxi>count?maxi:count;

        }
        return maxi;
}