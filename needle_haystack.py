# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# 28. Find the Index of the First Occurrence in a String

def strStr(haystack, needle):

    if len(needle) > len(haystack):
        return -1

    for ind, char in enumerate(haystack):
        if char == needle[0]:
            if len(haystack) >= ind + len(needle) and haystack[ind:ind +len(needle)] == needle:
                return ind

    return -1 



def test_1():
    assert strStr("sadbutsad","sad") == 0

def test_2():
    assert strStr("leetcode","leeto") == -1

def test_3():
    assert strStr("hello","ll") == 2

def test_3():
    assert strStr("aaa","aaaa") == -1

def test_4():
    assert strStr("mississippi","issip") == 4

def test_5():
    assert strStr("a","a") == 0