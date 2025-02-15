# https://leetcode.com/problems/plus-one/description/
# 66. Plus One

def plusOne(digits):
    carry = 0

    for ind, num in enumerate(reversed(digits)):
        if num == 9:
            carry = 1
            digits[len(digits)-ind-1] = 0
        else:
            digits[len(digits)-ind-1] = num + 1
            carry = 0

        if carry == 0:
            break

    if carry == 1:
        return [1] + digits

    return digits

def test_1():
    assert plusOne([1,2,3]) == [1,2,4]
def test_2():
    assert plusOne([4,3,2,1]) == [4,3,2,2]
def test_3():
    assert plusOne([9]) == [1,0]
def test_4():
    assert plusOne([8,9,9,9]) == [9,0,0,0]