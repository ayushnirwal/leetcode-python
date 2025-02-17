# https://leetcode.com/problems/intersection-of-multiple-arrays/
# 2248. Intersection of Multiple Arrays

def intersection(nums):
    dict = {}
    l = len(nums)

    res = []

    for num_arr in nums:
        for num in num_arr:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1

            if dict[num]>=l and num not in res:
                res.append(num)
    
    return sorted(res)
    
    

def test_1():
    assert intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]) == [3,4]

def test_2():
    assert intersection([[1,2,3],[4,5,6]]) == [] 

def test_3():
    assert intersection([[7,34,45,10,12,27,13],[27,21,45,10,12,13]]) == [10,12,13,27,45] 