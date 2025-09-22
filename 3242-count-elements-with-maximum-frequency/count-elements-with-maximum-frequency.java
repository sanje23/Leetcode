class Solution {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer,Integer>map = new HashMap<>();
        for(int i:nums){
            map.put(i,map.getOrDefault(i,0)+1);
        }
        int maxFreq=0;
        for(int i:map.values()){
            maxFreq=Math.max(maxFreq,i);
        }
        int res=0;
        for(int i:map.values()){
            if(maxFreq==i){
                res+=i;
            }
        }
        return res;
    }
}