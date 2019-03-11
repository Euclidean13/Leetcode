import numpy as np

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            if int(str(x)[::-1]) <= (2**31 - 1):
                return int(str(x)[::-1])
            else:
                return 0
        else:
            if int("-" + ''.join(list(str(x))[1:])[::-1]) >= -(2**31):
                return int("-" + ''.join(list(str(x))[1:])[::-1])
            else:
                return 0


# Test the object
obj = Solution()
print(obj.reverse(-1534233))
