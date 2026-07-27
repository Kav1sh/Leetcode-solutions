class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # outputS=""
        # for x in s:
        #     if x in outputS:
        #         return len(outputS) 
        #     else:
        #         outputS+=x
            # chars = set()
            # left = 0
            # max_length = 0
            # for x in range(len(s)):
            #     while s[x] not in chars:
            #         chars.add(s[x])
            #     elif s[x] in chars:
            #         chars.remove(s[x])
            #     return len(chars)
            chars = set()
            left = 0
            max_length = 0

            for x in range(len(s)):

                while s[x] in chars:
                    chars.remove(s[left])
                    left += 1

                chars.add(s[x])

                max_length = max(max_length, x - left + 1)

            return max_length