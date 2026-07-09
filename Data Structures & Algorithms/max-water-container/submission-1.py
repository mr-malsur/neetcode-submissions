class Solution:
    def maxArea(self, nums: List[int]) -> int:
        w , l , r = 0 , 0 , len(nums) - 1
        while l < r :
            area = min(nums[l],nums[r]) * (r-l)
            w = max(w,area)

            if nums[l] < nums[r] : l += 1
            else : r -= 1
        return w