class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr_diff = ( max(nums[:k]) - min(nums[:k]) )
        min_diff = curr_diff 
        for i in range(k,len(nums)) :
            curr_diff = nums[i] - nums[i-k+1]
            min_diff = min(min_diff,curr_diff)
        return min_diff 