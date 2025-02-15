def countQuadruplets(nums):

    res = 0
    n = len(nums)

    for i in range(0,n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                for l in range(k+1,n):
                    if nums[i] + nums[j] + nums[k] == nums[l]:
                        res+=1
    return res

print("[1,2,3,6]: ",countQuadruplets([1,2,3,6]))
print("[3,3,6,4,5]: ",countQuadruplets([3,3,6,4,5]))
print("[1,1,1,3,5]: ",countQuadruplets([1,1,1,3,5]))
