def canPlaceFlowers(flowerbed,n):

    copy_flowerbed = flowerbed[:]

    valid_places = 0
    length = len(copy_flowerbed)

    if length == 0:
        return False

    if length == 1 and copy_flowerbed[0]==0:
        return True

    if copy_flowerbed[0] == 0 and copy_flowerbed[1] == 0:
        valid_places+=1
        copy_flowerbed[0] = 1

    if copy_flowerbed[length-2] == 0 and copy_flowerbed[length-1] == 0:
        valid_places+=1
        copy_flowerbed[length-1] = 1

    for i in range( 1, length-1 ):
        if copy_flowerbed[i-1] == 0 and copy_flowerbed[i] == 0 and copy_flowerbed[i+1] == 0:
            valid_places+=1
            copy_flowerbed[i] = 1

    return n<=valid_places


print(" [1,0,0,0,1] , 1:", canPlaceFlowers([1,0,0,0,1],1))
print(" [1,0,0,0,0,1] , 2:", canPlaceFlowers([1,0,0,0,0,1],2))
print(" [0] , 1:", canPlaceFlowers([0],1))




