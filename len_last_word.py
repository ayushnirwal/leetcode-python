# https://leetcode.com/problems/length-of-last-word/description/
# 58. Length of Last Word

def lengthOfLastWord(s):
    len = 0
    for char in reversed(s.strip()):
        if char!=" ":
            len+=1
        else: break
    
    return len

def test_1 ():
    assert lengthOfLastWord("Hello World") == 5

def test_2 ():
    assert lengthOfLastWord("   fly me   to   the moon  ") == 4

def test_3 ():
    assert lengthOfLastWord("luffy is still joyboy") == 6

