# solution: BFS, 인접행렬방식이 아닌 인접리스트를 만들어 그래프를 탐색하는 문제였다.
# point: 이 문제는 BFS를 사용하면 풀리는 문제였다. 그러나 단순히 BFS를 적용하여 
#   모든 노드를 탐색한다면 메모리 초과가 발생하였다. 적절히 프루닝을 수행하여 불필요한 탐색(같은 노드 재방문)을
#   제거해주는 것이 중요하다.
# time-complexity: O(N)
# url: https://www.acmicpc.net/problem/18352

# start_input
import sys
input = sys.stdin.readline
N, M, K, X = map(int, input().rsplit())
adj_list = [[] for _ in range(N+1)]
for _ in range(M): 
    i, j = map(int, input().rsplit())
    adj_list[i].append(j)
# end_input

visited = [False for _ in range(N+1)]
result = []

from collections import deque
Q = deque()
Q.append((X, 0))

while Q:
    cur = Q.popleft()

    if cur[1] == K:
        if visited[cur[0]] == False:
            result.append(cur[0])
            visited[cur[0]] = True
        continue

    visited[cur[0]] = True

    for i in adj_list[cur[0]]:
        if visited[i] == False:
            Q.append((i, cur[1]+1))

if len(result) < 1: result.append(-1)
result.sort()

# start_print
for i in result: print(i)
# end_print