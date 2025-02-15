def twoSum(nums,target):
    # Make hasmap for number to be added to achieve target with indexes

    targetMap={}
    for i, num in enumerate(nums):
        targetMap[target-num] = i

    # Loop through numbers and find second number's index
    for i, num in enumerate(nums):
        if num in targetMap.keys() and targetMap[num] != num:
            return [i,targetMap[num]]
        
print(twoSum([2,7,11,15],9))
