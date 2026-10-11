class Solution {
public:
    void reverse(vector <char> &s,int i, int j){
        if (i >=j) return;
        int temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        reverse(s,++i,--j);
    }
	vector<char> reverseString(vector<char>& s){
		//your code goes here
        reverse(s,0,s.size()-1);
        return s;

	}
};