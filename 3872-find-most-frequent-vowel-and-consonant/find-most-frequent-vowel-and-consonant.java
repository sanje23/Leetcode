class Solution {
    public int maxFreqSum(String s) {
        int[] arr = new int[27];
        for(char i:s.toCharArray()){
            arr[Character.toLowerCase(i)-'a']++;
        }
        int t=0;
        int q=0;
        for(int i=0;i<27;i++){
            if(i!=0 && i!=4 && i!=8 && i!=14 && i!=20){
                q=Math.max(q,arr[i]);
            }
            else{
                t=Math.max(t,arr[i]);
            }
        }
        return q+t;
    }
}