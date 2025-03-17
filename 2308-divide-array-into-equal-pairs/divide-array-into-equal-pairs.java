class Solution {
    public boolean divideArray(int[] nums) {
        HashMap<Integer,Integer>freq=new HashMap<>();
        for(int i:nums){
            freq.put(i,freq.getOrDefault(i,0)+1);
        }
        for(var i:freq.entrySet()){
            if((i.getValue())%2!=0){
                return false;
            }
        }
        return true;
    }
}