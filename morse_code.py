# https://leetcode.com/problems/unique-morse-code-words/description/
# 804. Unique Morse Code Words

codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

def wordToCode(word):
    res = ""
    for letter in word:
        res += codes[ord(letter) - ord("a")]
    return res

def uniqueMorseRepresentations(words):
    res = set() 
    for word in words:
        res.add(wordToCode(word))
    
    return len(res)

def test_1():
    assert(uniqueMorseRepresentations(["gin","zen","gig","msg"])) == 2

def test_2():
    assert(uniqueMorseRepresentations(["a"])) == 1
