class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c , mc = 0 , 0 
        for i in nums :
            if i == 1 :
                c += 1
                mc = max(mc,c)
            else :
                c = 0
        return mc