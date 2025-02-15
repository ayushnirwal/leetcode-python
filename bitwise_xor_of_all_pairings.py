def xorAllNums(nums1, nums2):
    res = 0
    if len(nums2) % 2 != 0:
        for num in nums1:
            res = res^num

    if len(nums1) % 2 != 0:
        for num in nums2:
            res = res^num
    return res



def test_1():
    assert xorAllNums([2,1,3],[10,2,5,0]) == 13

def test_2():
    assert xorAllNums([1,2],[3,4]) == 0