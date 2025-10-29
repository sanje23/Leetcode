class Solution {
    public int smallestNumber(int n) {
        int res=1;
        while(n>res){
            res = (res<<1) | 1;
        }
        return res;
    }
}