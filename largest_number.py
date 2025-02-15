# https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2025-01-30
# 179. Largest Number
from functools import cmp_to_key

def compare(a,b):
    num_a = a * pow(10,len(str(b))) + b
    num_b = b * pow(10,len(str(a))) + a

    if int(num_a) > int((num_b)):
        return 1
    elif int(num_a) < int((num_b)):
        return -1
    else:
        return 0
    

def largestNumber(nums):
    res = ""
    for num in sorted(nums,key=cmp_to_key(compare)):
        print(num)
        res = str(num) + res

    return str(int(res))


# def test_01():
#     assert compare(3,30) == True

# def test_02():
#     assert compare(34323, 3432) == 1

def test_1():
    assert largestNumber([10,2]) == "210"

def test_2():
    assert largestNumber([3,30,34,5,9]) == "9534330"

def test_3():
    assert largestNumber([34323, 3432]) == "343234323"

def test_4():
    assert largestNumber([0,0]) == "0"