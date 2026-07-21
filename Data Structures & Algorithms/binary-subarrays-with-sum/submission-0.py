class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(nums,k) :
            if k < 0 :
                return 0

            l = 0
            curr_count = 0 
            ans = 0

            for r in range(len(nums)) :
                curr_count += nums[r]

                while curr_count > k :
                    curr_count -= nums[l]
                    l += 1
                ans += (r-l+1)
            return ans 
        return atmost(nums,goal) - atmost(nums,goal-1)