class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(nums,k) :
            l = 0
            count = 0
            hm = {}

            for r in range(len(nums)) :
                hm[nums[r]] = hm.get(nums[r],0) + 1

                while len(hm) > k :
                    hm[nums[l]] -= 1
                    if hm[nums[l]] == 0 :
                        del hm[nums[l]]
                    l += 1
                count += (r - l + 1)
            return count 
        return atmost(nums,k) - atmost(nums,k-1)