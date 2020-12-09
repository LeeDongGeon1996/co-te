# solution: DFS로 해결을 시도해보았지만 테스트케이스는 통과하였으나, 히든 케이스에서
#   시간 초과가 난다. BFS로 시도 할 것.
# time-complexity: N/A
# url: https://www.acmicpc.net/problem/16234

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, L, R = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]

# E, W, S, N
move_x = [1, -1, 0, 0]
move_y = [0, 0, 1, -1] 

sum = 0
def dfs(i, j):
    global sum

    union.append((i,j))
    sum += _map[i][j]
    _visited[i][j] = cnt
    for dir in range(4):
        x_moved = j + move_x[dir]
        y_moved = i + move_y[dir]
        if 0 <= x_moved < N and 0 <= y_moved < N:
            if _visited[y_moved][x_moved] < cnt and \
                L <= abs(_map[i][j] - _map[y_moved][x_moved]) <= R:
                dfs(y_moved, x_moved)

cnt = -1
beContinue = True
union = []
_visited = [[-1]*N for _ in range(N)]
while beContinue:
    cnt += 1
    beContinue = False
    for i in range(N):
        for j in range(N):
            if _visited[i][j] < cnt:
                sum = 0
                union.clear()
                dfs(i,j)
                if len(union) > 1:
                    beContinue = True
                    for c in union: _map[c[0]][c[1]] = sum//len(union)

print(cnt)