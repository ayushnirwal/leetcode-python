offset = ord("a") - ord("A")

def checkIfLettersPresent(str1,str2):
    flag = True
    for c in str1:
        if str2.find(c)>=0:
            continue
        else:
            flag = False
            break
    return flag

def test(words):
    res = []
    rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
    for word in words:
        if checkIfLettersPresent(word.lower(),rows[0]) or checkIfLettersPresent(word.lower(),rows[1]) or checkIfLettersPresent(word.lower(),rows[2]):
            res.append(word)
    return res


inputs = [
    ["Hello","Alaska","Dad","Peace"],
    ["a","b"],
]        

outputs = [
    ["Alaska","Dad"],
    ["a","b"],
]        

for ind,input in enumerate(inputs):
    output = outputs[ind]
    print(test(input),output)
