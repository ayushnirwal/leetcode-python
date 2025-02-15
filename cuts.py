# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/
# 3394. Check if Grid can be Cut into Sections

checkCut = lambda cut, n : cut !=0 and cut !=n
checkRectangle = lambda lb, ub, y1, y2 : y1 >= lb and y2 <= ub
hasConflict = lambda  a,b : b[0]>=a[0] and b[0]< a[1] 

def merge(intervals):
    res = []
    intervals = sorted(intervals, key=lambda x: x[0])

    for interval in intervals:
        if len(res) == 0:
            res.append(interval)
            continue

        last_interval = res[len(res) - 1]
        if hasConflict(last_interval,interval):
            res.pop()
            res.append([last_interval[0],max(last_interval[1],interval[1])])
        else: 
            res.append(interval)
        

    return res

def checkValidCuts(n,rectangles):
    v_cuts_pair = [] 
    h_cuts_pair = [] 

    for rectangle in rectangles:
        h_cuts_pair.append([rectangle[0],rectangle[2]])
        v_cuts_pair.append([rectangle[1],rectangle[3]])

    merged_h = merge(h_cuts_pair)
    merged_v = merge(v_cuts_pair)

    print(h_cuts_pair , " : " , merged_h)
    print(v_cuts_pair , " : " , merged_v)

    return len(merged_h) >= 3 or len(merged_v) >= 3




def test_1():
    assert checkValidCuts(5,[[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]) == True

def test_2():
    assert checkValidCuts(4,[[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]) == True

def test_3():
    assert checkValidCuts(4,[[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]) == False

def test_4():
    assert checkValidCuts(6,[[4,0,5,2],[0,5,4,6],[4,5,6,6]]) == False

def test_5():
    assert checkValidCuts(9,[[0,0,1,7],[1,0,5,6],[5,0,7,6],[7,0,8,6],[8,0,9,6],[1,6,9,7],[0,7,9,8],[0,8,9,9]]) == True

def test_6():
    assert checkValidCuts(4,[[0,0,1,4],[1,0,2,4],[2,0,3,4],[3,0,4,4]]) == True