def isPalindrome(x):

    # Negative numbers can't be pallindromes
    if x < 0:
        return False

    # Convert number into an array
    _x = x
    a=[]
    while _x>0:
        a.append(_x%10)
        _x=_x//10

    # Compare numbers in array form start and end with equal offset
    flag = True

    for i in range(0,len(a)//2):
        if a[i]!=a[len(a)-i-1]:
            flag = False
            break

    return flag

print(isPalindrome(101))
