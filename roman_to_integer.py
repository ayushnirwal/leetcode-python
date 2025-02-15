def romanToInt(s):

    # Lookup table to know letter value
    lookUp = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    # Convert string to number array for later calculation

    numList = []

    for c in s:
        numList.append(lookUp[c])

    i = 0
    res = 0
    while (i < len(numList)-1):
        # if the next number is larger just add the current number
        if numList[i] >= numList[i+1]:
            res += numList[i]
            i+=1 
        # if the next number is smaller subtract next number from 
        # current number then add it to result variable and move one extra index
        else:
            res += numList[i+1]-numList[i]
            i+=2
    if i == len(numList) - 1:
        res+= numList[i]
    
    return res


print(romanToInt("MCMXCIV"))
