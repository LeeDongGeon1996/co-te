# solution: BFS로 시도. Python3로는 시간 초과, Pypy3로 해결..
# time-complexity: O(N^2 + V), E는 edge의 수 
# url: https://www.acmicpc.net/problem/16234

import sys
input = sys.stdin.readline
N, L, R = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]

# E, W, S, N
move_x = [1, -1, 0, 0]
move_y = [0, 0, 1, -1] 

_visited = [[-1]*N for _ in range(N)]
cnt = -1
sum = 0
from collections import deque
def bfs(i,j):
    global cnt, sum
    
    Q = deque([(i,j)])
    _visited[i][j] = cnt

    while Q:
        cur = Q.popleft()
        sum += _map[cur[0]][cur[1]]
        union.append(cur)

        for dir in range(4):
            x_moved = cur[1] + move_x[dir]
            y_moved = cur[0] + move_y[dir]
            if 0 <= x_moved < N and 0 <= y_moved < N:
                if _visited[y_moved][x_moved] < cnt and (L <= abs(_map[cur[0]][cur[1]] - _map[y_moved][x_moved]) <= R):
                    _visited[y_moved][x_moved] = cnt
                    Q.append((y_moved,x_moved))


union = []
beContinue = True
while beContinue:
    beContinue = False
    cnt += 1
    for i in range(N):
        for j in range(N):
            if _visited[i][j] < cnt:
                union.clear()
                sum = 0
                bfs(i,j)
                if len(union) > 1:
                    beContinue = True
                    for c in union: _map[c[0]][c[1]] = sum//len(union)

print(cnt)