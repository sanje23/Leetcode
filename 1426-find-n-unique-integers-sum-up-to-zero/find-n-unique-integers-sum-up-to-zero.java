class Solution {
    public int[] sumZero(int n) {
        int t=n/2;
        int[] res = new int[n];
        int index=0;
        for(int i=1;i<=t;i++){
            res[index++]=i;
            res[index++]=-i;
        }
        if(n%2!=0){
            res[index]=0;
        }
        return res;
    }
}