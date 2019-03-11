class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        array_s = list(s)
        middle_result = []
        result = []

        for i in array_s:
            middle_result.append(i)
            if middle_result.count(i) > 1:
                middle_result = middle_result[int(''.join(middle_result).find(i))+1:].copy()

            if len(middle_result) > len(result):
                result = middle_result.copy()

        return len(result)


# Testing the object
obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))
