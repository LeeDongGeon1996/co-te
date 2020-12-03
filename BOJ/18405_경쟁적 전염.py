# solution: BFS, 바이러스부터가 아닌 주어진 좌표에서 부터 BFS를 시작하면 더 효율적이다. 
#   가장 먼저 만나게 되는 바이러스가 S초후 감염될 바이러스라고 생각할 수 있다. 
#   S초까지 바이러스를 만나지 못하면 감염되지 않는다는 것이다.
# time-complexity: O(N^2)
# url: https://www.acmicpc.net/problem/18405

# start_input
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
# end_input

# E, W, S, N
move_x = [1, -1, 0, 0]
move_y = [0, 0, 1, -1]

result = K+1

from collections import deque
Q = deque()
Q.append((X-1, Y-1, 0))

if _map[X-1][Y-1] != 0:
    result = _map[X-1][Y-1]
    Q.clear()

while Q:
    cur = Q.popleft()
    if cur[2] == S:
        break
    for i in range(4):
        x_moved = cur[1] + move_x[i]
        y_moved = cur[0] + move_y[i]
        
        if x_moved < 0 or x_moved >= N or y_moved < 0 or y_moved >= N:
            continue

        if _map[y_moved][x_moved] == 0:
            _map[y_moved][x_moved] = -1
            Q.append((y_moved,x_moved, cur[2] + 1))
        elif _map[y_moved][x_moved] > 0:
            if result > _map[y_moved][x_moved]: 
                result = _map[y_moved][x_moved]
                S = cur[2] + 1

    
if result == K+1:
    result = 0

# start_print
print(result)
# end_print