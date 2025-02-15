# https://leetcode.com/problems/add-binary/description/
# 67. Add Binary

def addBinary(a,b):

    if len(a) < len(b):
        a = a.zfill(len(b))
    else:
        b = b.zfill(len(a))

    res = ""
    carry = "0"

    for ind in range(0,len(a)):
        d1 = a[len(a) - ind - 1]
        d2 = b[len(b) - ind - 1]

        sum = int(d1) + int(d2) + int(carry)

        res += str(sum % 2)
        carry = "0" if sum < 2 else "1"

    if carry == "1":
        res = res + carry

    return res[::-1]

def test_1():
    assert addBinary("11","1") == "100"

def test_2():
    assert addBinary("1010","1011") == "10101"

def test_3():
    assert addBinary("0","0") == "0"