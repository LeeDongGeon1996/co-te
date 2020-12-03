# solution: dfs로 해결(이 문제의 경우 잘못된 접근방식..)
# time-complexity: O(S*N^2)
# url: https://www.acmicpc.net/problem/18405

# start_input
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
# end_input

visited = [[-1]*N for _ in range(N)]
def dfs(x, y, sec, virus):
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if visited[x][y] < sec:
        visited[x][y] = sec
        if _map[x][y] == 0:
            _map[x][y] = virus
        elif _map[x][y] == virus:
            dfs(x-1, y, sec, virus)
            dfs(x+1, y, sec, virus)
            dfs(x, y-1, sec, virus)
            dfs(x, y+1, sec, virus)

    elif visited[x][y] == sec:
        if _map[x][y] > virus:
            _map[x][y] = virus


for sec in range(S):
    for i in range(N):
        for j in range(N):
            if _map[i][j] > 0 and visited[i][j]!=sec:
                dfs(i, j, sec, _map[i][j])

# start_print
print(_map[X-1][Y-1])
# end_print