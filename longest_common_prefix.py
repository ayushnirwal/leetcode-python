def longestCommonPrefix(strs):
    res = "" 
    minLen = 300 

    for str in strs:
        if minLen > len(str):
            minLen = len(str)

    for i in range(0,minLen):

        letter = strs[0][i]
        flag = True

        for strInd in range(1,len(strs)):
            if strs[strInd][i] != letter:
                flag = False
                break

        if flag:
            res+=letter
        else:
            break


    print(res)


longestCommonPrefix(["c","acc","ccc"])
                



