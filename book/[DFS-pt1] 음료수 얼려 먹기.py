# solution: DFS로 붙어있는 칸을 모두 하나로 묶어 방문처리한다.
# time-complexity: O(N^2)

# start_input
N, M = map(int, input().split())
_map = [list(map(int, input())) for _ in range(N)]
# end_input

def dfs(r,c):

    if r < 0 or r >= N or c < 0 or c >= M:
        return False

    if _map[r][c] == 0:
        _map[r][c] = 1
        dfs(r-1,c)
        dfs(r+1,c)
        dfs(r,c-1)
        dfs(r,c+1)
        return True
    return False

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
             cnt += 1

# start_print
print(cnt)
# end_print
