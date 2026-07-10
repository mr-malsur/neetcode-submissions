class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        r1 , r2 , res = [] , [] , [] 
        for i in nums :
            if i < 0 :
                r2.append(i)
            else :
                r1.append(i)
        l , r = 0 , 0
        while l < n//2 :
            res.append(r1[l])
            res.append(r2[r])
            l += 1
            r += 1
        return res