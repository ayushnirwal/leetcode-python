import math

def searchInsert(nums, target):
    lower = 0
    upper = len(nums)-1

    while lower < upper:
        
        ind = (lower + upper )//2

        if nums[ind] == target:
            return ind
        
        elif nums[ind] < target:
            # Go right
            if ind < len(nums) - 1:
                lower = ind + 1
            else:
                break
        
        elif nums[ind] > target:
            # Go left
            if ind > 0:
                upper = ind - 1
            else:
                break

    ind = (lower + upper )//2
    if nums[ind] < target:
        return ind+1
    return ind 

