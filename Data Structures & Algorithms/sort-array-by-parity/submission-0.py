class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        r1 , r2 = [] , []
        for i in nums :
            if i % 2 == 0 :
                r1.append(i)
            else :
                r2.append(i)
        return r1 + r2