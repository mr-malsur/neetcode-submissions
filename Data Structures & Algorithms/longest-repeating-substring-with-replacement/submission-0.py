class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l = 0
        max_len = float('-inf')

        for r in range(len(s)) :
            hashmap[s[r]] = hashmap.get(s[r],0) + 1
            while r-l+1 - max(hashmap.values()) > k :
                hashmap[s[l]] -= 1
                if hashmap[s[l]] == 0 :
                    del hashmap[s[l]]
                l += 1
            max_len = max(max_len,r-l+1)
        return max_len