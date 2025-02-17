# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/description/
# 3418. Maximum Amount of Money Robot Can Earn

def maximumAmount(coins):
    m, n = len(coins), len(coins[0])
    dp = [[[float('-inf')]*3 for _ in range(n)] for _ in range(m)]

    dp[0][0][2] = coins[0][0]
    if coins[0][0] < 0: dp[0][0][1] = 0

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            for k in range(3):
                if i == m-1 and j == n-1:
                    dp[i][j][k] = max(0, coins[i][j]) if k > 0 else coins[i][j];
                    continue;

                ans = float("-inf")

                if i < m - 1:
                    # if no neutralization is benificial
                    ans = max(ans, dp[i+1][j][k] + coins[i][j]) 
                    # if eutralization is benificial
                    if k>0 : ans = max(ans, dp[i+1][j][k-1])

                if j < n - 1:
                    # if no neutralization is benificial
                    ans = max(ans, dp[i][j+1][k] + coins[i][j]) 
                    # if eutralization is benificial
                    if k>0 : ans = max(ans, dp[i][j+1][k-1])
                
                dp[i][j][k] = ans
    for i in range(m):
        print(dp[i][::][::])

    return dp[0][0][2]






# def test_1():
#     assert maximumAmount([[0,1,-1],[1,-2,3],[2,-3,4]]) == 8

# def test_2():
#     assert maximumAmount([[10,10,10],[10,10,10]]) == 40

# def test_3():
#     assert maximumAmount([[-4]]) == 0

# def test_4():
#     assert maximumAmount([[-16,8,-7,-19],[6,3,-10,13],[13,15,4,-3],[-16,4,19,-12]]) == 57

def test_5():
    assert maximumAmount([[-7,12,12,13],[-6,19,19,-6],[9,-2,-10,16],[-4,14,-10,-9]]) == 60