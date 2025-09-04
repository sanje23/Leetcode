class Solution {
    public int findClosest(int x, int y, int z) {

        int s=Math.abs(z-x);
        int t=Math.abs(z-y);

        int q=Math.min(s,t);

        if(t==s){
            return 0;
        }
        else if(q==t){
            return 2;
        }
        return 1;
    }
}