class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        l = 0
        mul = 1

        if k <= 1 :
            return 0

        for r in range(len(nums)) :
            mul *= nums[r]
            while mul >= k :
                mul //= nums[l]
                l += 1 
            count += (r-l+1)
        return count