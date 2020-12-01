# solution: dfs, 벽을 세울 수 있는 조합을 구해서 각 조합으로 벽을 세운뒤,
#   safe한 칸의 수를 센다.
# time-complexity: O(N^2)
# url: https://www.acmicpc.net/problem/14502

# start_input
N, M = map(int, input().split())
_map = []
for i in range(N):
    _map.append(list(map(int, input().split())))
# end_input

from itertools import combinations
ept = []
for i in range(N):
    for j in range(M):
        if _map[i][j] == 0:
            ept.append((i,j))
comb = combinations(ept, 3)

safe_cnt = 0
contaminated = False
def dfs(i, j, visited):
    global safe_cnt, contaminated

    if i < 0 or i >= N or j < 0 or j >= M:
        return

    if _map[i][j] != 1 and visited[i][j] == False:
        visited[i][j] = True  
        if _map[i][j] == 0:
            safe_cnt += 1
        elif _map[i][j] == 2:
            contaminated = True
        
        dfs(i-1, j, visited)
        dfs(i+1, j, visited)
        dfs(i, j-1, visited)
        dfs(i, j+1, visited)

result = 0
for c in comb:
    for wall in c: _map[wall[0]][wall[1]] = 1

    visited = [[False]*M for _ in range(N)]
    safe_total = 0

    for i in range(N):
        for j in range(M):
            safe_cnt = 0
            contaminated = False
            dfs(i, j, visited)
            if not contaminated: safe_total += safe_cnt

    for wall in c: _map[wall[0]][wall[1]] = 0
    if result < safe_total: result = safe_total
        
# start_print
print(result)
# end_print