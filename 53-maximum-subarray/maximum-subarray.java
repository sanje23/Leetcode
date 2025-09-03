class Solution {
    public int maxSubArray(int[] nums) {

        int maxSum=nums[0],currSum=nums[0];

        for(int i=1;i<nums.length;i++){
            currSum+=nums[i];
            currSum=Math.max(currSum,nums[i]);
            maxSum=Math.max(currSum,maxSum);
        }
        return maxSum;
        
    }
}