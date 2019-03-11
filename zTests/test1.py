"""
Script used for testing purposes
"""
x = -12
b = list(str(x))[1:]
print(b)
y = int("-" + ''.join(list(str(x))[1:])[::-1])
print(y)

print((2**31 - 1)/2)