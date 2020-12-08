# solution: dfs, 한 방향으로만 탐색을 하는 것이 관건이었다.
# time-complexity: O(N + T) - T는 주어진 T의 갯수
# url: https://www.acmicpc.net/problem/18428

# start_input
N = int(input())
_map = [input().split() for _ in range(N)]
# end_input

# E, W, S, N
move_x = [1, -1, 0, 0]
move_y = [0, 0, 1, -1]

spaces = []
teachers = []
for i in range(N):
    for j in range(N):
        if _map[i][j] == 'X': spaces.append((i,j))
        elif _map[i][j] == 'T': teachers.append((i,j))

from itertools import combinations
comb = combinations(spaces, 3)

detected = False
def dfs(i, j, dir):
    global detected

    x_moved = j + move_x[dir]
    y_moved = i + move_y[dir]

    if y_moved < 0 or y_moved >= N or x_moved < 0 or x_moved >= N:
        return
    
    if _map[y_moved][x_moved] == 'S':
        detected = True
    elif _map[y_moved][x_moved] == 'X':
        dfs(y_moved, x_moved, dir)


def main():
    global detected
    for walls in comb:
        detected = False
        for wall in walls: _map[wall[0]][wall[1]] = 'O'
        for t in teachers: 
            for dir in range(4): 
                dfs(t[0], t[1], dir)
                if detected:
                    break
            if detected:
                break
        if not detected:
            print("YES")
            return

        for wall in walls: _map[wall[0]][wall[1]] = 'X'

    print("NO")

# start_print
main()
# end_print