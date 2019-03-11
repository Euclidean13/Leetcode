class Solution:
    def convert(self, s: str, numRows: int) -> str:
        flag = True
        number = 0
        middle_num = 0
        forward = True

        rows = ["" for row in range(numRows)]
        print(rows)

        for i, a in enumerate(s):
            if number == i and flag is True:
                rows[0] = rows[0] + a
                number += numRows -1
                flag = False
            elif number == i and flag is False:
                rows[numRows-1] = rows[numRows-1] + a
                number += numRows - 1
                flag = True
            else:
                if forward is True and numRows>1:
                    middle_num += 1
                    rows[middle_num] = rows[middle_num] + a
                    if middle_num >= numRows-2:
                        forward = False
                elif forward is False and numRows>1:
                    rows[middle_num] = rows[middle_num] + a
                    if middle_num <= 1:
                        forward = True
                    middle_num -= 1
                else:
                    rows.append(a)

        return ''.join(rows)


# Testing the object
obj = Solution()
input_string = "PAYPALISHIRING"
num_Rows = 3
print(obj.convert(input_string, num_Rows))