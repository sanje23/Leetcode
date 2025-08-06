class Solution {
public:
    bool isPalindrome(int x) {
        double t=0;
        int s=x;
        while(x>0){
            int q=x%10;
            t=(t*10)+q;
            x/=10;
        }
        return s==t;
        
    }
};