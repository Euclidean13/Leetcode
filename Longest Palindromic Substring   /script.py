class Solution:
    def longestPalindrome(self, s: str) -> str:
        l_substring = ""
        for i in range(len(s)):
            for j in range(len(s)):
                forward = s[i:j+1]

                if forward == forward[::-1] and len(forward) > len(l_substring):
                    l_substring = forward
        return l_substring


# Testing the object
obj = Solution()
print(obj.longestPalindrome("babad"))