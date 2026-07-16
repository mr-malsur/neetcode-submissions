class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = 0
        curr_len = 0
        max_len = 0
        for r in range(len(s)) :
            curr_len += 1

            while s[r] in hashset :
                hashset.remove(s[l])
                l += 1

            max_len = max(max_len,r-l+1)
            hashset.add(s[r])
        return max_len  