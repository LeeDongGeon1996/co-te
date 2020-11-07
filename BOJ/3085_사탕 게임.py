# solution: brute-force, 모든 경우의 수를 직접 시도해본다.
# time-complexity: O(N^2)
# url: https://www.acmicpc.net/problem/3085

# 문제오류: "상근이는 사탕의 색이 다른 인접한 두 칸을 고른다."라고 써있지만
# {색이 다른 칸이 아닌 경우}를 제외하고 탐색한다면 테스트 케이스를 통과하지 못한다...;

# start_input
N = int(input())
candys = []
for i in range(N):
    candys.append(list(input()))
# end_input

max = 1
def compare(i, j):
    global max
    el = candys[i][j]
    cnt = 1

    #left
    idx = 1
    next_val = candys[i][j-idx] if j-idx >= 0 else None
    while next_val != None and el == next_val:
        cnt += 1
        idx += 1
        next_val = candys[i][j-idx] if j-idx >= 0 else None
    
    #right
    idx = 1
    next_val = candys[i][j+idx] if j+idx < N else None
    while next_val != None and el == next_val:
        cnt += 1
        idx += 1
        next_val = candys[i][j+idx] if j+idx < N else None
    
    if max < cnt:
        max = cnt
            
    cnt = 1
    #up
    idx = 1
    next_val = candys[i-idx][j] if i-idx >= 0 else None
    while next_val != None and el == next_val:
        cnt += 1
        idx += 1
        next_val = candys[i-idx][j] if i-idx >= 0 else None
    
    #down
    idx = 1
    next_val = candys[i+idx][j] if i+idx < N else None
    while next_val != None and el == next_val:
        cnt += 1
        idx += 1
        next_val = candys[i+idx][j] if i+idx < N else None
    
    if max < cnt:
        max = cnt
        

for i in range(N):
    for j in range(N-1):
        #h
        candys[i][j], candys[i][j+1] = candys[i][j+1], candys[i][j]
        compare(i, j)
        compare(i, j+1)
        candys[i][j], candys[i][j+1] = candys[i][j+1], candys[i][j]

        #v
        candys[j][i], candys[j+1][i] = candys[j+1][i], candys[j][i]
        compare(j, i)
        compare(j+1, i)
        candys[j][i], candys[j+1][i] = candys[j+1][i], candys[j][i]

# start_print
print(max)
# end_print