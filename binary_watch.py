# https://leetcode.com/problems/binary-watch/description/
# 401. Binary Watch

def readBinaryWatch(turnedOn):
    res = []

    for h in range(12):  # Hours: 0-11
        for m in range(60):  # Minutes: 0-59
            if bin(h).count("1") + bin(m).count("1") == turnedOn:
                res.append("{}:{:02d}".format(h, m))
    
    return res


def test_1():
    assert readBinaryWatch(1) == ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

def test_2():
    assert readBinaryWatch(9) == []