# https://leetcode.com/problems/available-captures-for-rook/
# 999. Available Captures for Rook

def numRookCaptures(board):
    # Find rook
    Ri = -1
    Rj = -1

    res = 0

    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] == 'R':
                Ri = i
                Rj = j
    
    
    # Traverse up
    Ri_buf = Ri
    Rj_buf = Rj

    while Ri_buf > 0:
        Ri_buf -= 1
        if board[Ri_buf][Rj_buf] == ".":
            continue
        elif board[Ri_buf][Rj_buf] == "p":
            res += 1
            break
        elif board[Ri_buf][Rj_buf] == "B":
            break
    

    # Traverse down
    Ri_buf = Ri
    Rj_buf = Rj

    while Ri_buf < 7:
        Ri_buf += 1
        print(Ri_buf)
        if board[Ri_buf][Rj_buf] == ".":
            continue
        elif board[Ri_buf][Rj_buf] == "p":
            res += 1
            break
        elif board[Ri_buf][Rj_buf] == "B":
            break

    # Traverse left
    Ri_buf = Ri
    Rj_buf = Rj

    while Rj_buf >0:
        Rj_buf -= 1
        if board[Ri_buf][Rj_buf] == ".":
            continue
        elif board[Ri_buf][Rj_buf] == "p":
            res += 1
            break
        elif board[Ri_buf][Rj_buf] == "B":
            break

    # Traverse right
    Ri_buf = Ri
    Rj_buf = Rj

    while Rj_buf < 7:
        Rj_buf += 1
        if board[Ri_buf][Rj_buf] == ".":
            continue
        elif board[Ri_buf][Rj_buf] == "p":
            res += 1
            break
        elif board[Ri_buf][Rj_buf] == "B":
            break

    return res


def test_1():
    assert numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]) == 3

def test_2():
    assert numRookCaptures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]) == 0

def test_3():
    assert numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]) == 3

def test_4():
    assert numRookCaptures([[".",".",".",".",".",".",".","."],
                            [".",".",".",".",".",".",".","."],
                            [".",".",".",".",".",".",".","."],
                            [".",".",".","R",".",".",".","."],
                            [".",".",".",".",".",".",".","."],
                            [".",".",".",".",".",".",".","."],
                            [".",".",".",".",".",".",".","."],
                            [".",".",".",".",".",".",".","."]]) == 0