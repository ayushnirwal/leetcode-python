# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number

def letterCombinations(digits):
    dict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    res = []

    for digit in digits:
        if len(res) == 0:
            for alpha in dict[digit]:
                res.append(alpha)
        else:
            buf = []
            for alpha in dict[digit]:
                for ele in res:
                    buf.append(ele + alpha)
            res = buf
        print(digit, res)

    return res


def test_1():
    assert set(letterCombinations("23")) == set(["ad","ae","af","bd","be","bf","cd","ce","cf"])

def test_2():
    assert letterCombinations("") == []

def test_3():
    assert letterCombinations("2") == ["a","b","c"]
