# https://leetcode.com/problems/merge-intervals/description/
# 56. Merge Intervals

hasConflict = lambda  a,b : b[0]>=a[0] and b[0]<= a[1] 

def merge(intervals):
    res = []
    intervals = sorted(intervals, key=lambda x: x[0])

    for interval in intervals:
        if len(res) == 0:
            res.append(interval)
            continue

        last_interval = res[len(res) - 1]
        print(last_interval,interval,hasConflict(last_interval,interval) )
        if hasConflict(last_interval,interval):
            res.pop()
            res.append([last_interval[0],max(last_interval[1],interval[1])])
        else: 
            res.append(interval)
        

    return res
        

def test_1():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

def test_2():
    assert merge([[1,4],[4,5]]) == [[1,5]]

def test_3():
    assert merge([[1,4],[1,4]]) == [[1,4]]

def test_4():
    assert merge([[1,4],[2,3]]) == [[1,4]]