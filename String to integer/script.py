class Solution:
    def myAtoi(self, str: str) -> int:
        # Lets first delete the white spaces
        strWS = str.replace(' ', '')

        # Then transform the str into an array
        strAWS = list(strWS)
        print(len(strAWS))

        if str=="":
            return 0

        # Read each elements to take only the numerical characters in case exists
        resultA = []
        for a in strAWS:
            print(a)
            if a == '-' or a.isdigit() is True and len(strAWS) > 1:
                resultA.append(a)
            else:
                return 0

        resultAS = int(''.join(resultA))
        if resultAS >= (2**31-1):
            return 2**31-1
        elif resultAS <= -(2**31):
            return -(2**31)
        else:
            return resultAS

# Testing the object
obj = Solution()
print(obj.myAtoi("-"))