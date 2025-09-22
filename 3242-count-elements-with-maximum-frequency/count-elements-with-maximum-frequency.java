class Solution {
    public int maxFrequencyElements(int[] nums) {
        
        Map<Integer,Integer>freq= new HashMap<>();
        for(int i:nums){
            freq.put(i,freq.getOrDefault(i,0)+1);
        }
        int maxFreq=0;
        for(int count:freq.values()){
            maxFreq=Math.max(count,maxFreq);
        }
        int res=0;
        for(int i:freq.values()){
            if(i==maxFreq){
                res+=i;
            }
        }
        return res;
    }
}