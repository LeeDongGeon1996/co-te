# solution: 괴물이 있는 곳은 0, 없는 곳은 1 / 최소경로는 같은 장소를 두번 방문하는 일이 없음.
#    방문한 곳의 값을 -1해서 괴물이 있는 것처럼 만들면서 BFS를 수행한다.
# time-complexity: O(N^2)

# start_input
N, M = map(int, input().split())
_map = [list(map(int, input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
# end_input

# E, W, S, N
move_x = [1, -1, 0, 0]
move_y = [0, 0, 1, -1]

result = -1

from collections import deque
Q = deque()
Q.append((0, 0, 1))

while Q:
    cur = Q.popleft()
    _map[cur[1]][cur[0]] -= 1
    for i in range(4):
         x_moved = cur[0] + move_x[i]
         y_moved = cur[1] + move_y[i]

         if x_moved > -1 and x_moved < M and y_moved > -1 and y_moved < N \
             and _map[y_moved][x_moved] > 0:
             next_pos = (x_moved, y_moved, cur[2] + 1)
             Q.append(next_pos)
             if next_pos[0] == M-1 and next_pos[1] == N-1:
                 result = next_pos[2]
                 Q.clear()
             
# start_print
print(result)
# end_input
