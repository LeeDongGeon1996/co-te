# solution: 맵의 테두리를 이동 할 수 없는 상수(1)로 대체한다.
#   0: 이동가능, 1: 바다, 2: 이미 가 본 칸
#   
# time-complexity: O(N^2)...? 맵의 칸 갯수만큼의 시간복잡도를 갖는다. 라고 생각한다....

# [U, R, D, L]
move_x = [0, 1, 0, -1]
move_y = [-1, 0, 1, 0]

# start_input
R, C = map(int, input().split())
x_pos, y_pos, dir = map(int, input().split())
_map = []
for i in range(R):
    _map.append(list(map(int,input().split())))
# end_input

# Map 테두리 보정
for row in _map:
    row.insert(0, 1)
    row.append(1)
_map.insert(0, [1]*(C+2))
_map.append([1]*(C+2))
x_pos += 1
y_pos += 1

cnt = 1 if _map[y_pos][x_pos] == 0 else 0
_map[y_pos][x_pos] = 2

is_possible = True
while is_possible:
    is_possible = False

    for i in range(4):
        dir = (dir + 3) % 4
        x_moved = x_pos + move_x[dir]
        y_moved = y_pos + move_y[dir]
        
        if _map[y_moved][x_moved] == 0:
            x_pos = x_moved
            y_pos = y_moved
            _map[y_pos][x_pos] = 2
            cnt += 1
            is_possible = True
            break
    
    if is_possible == False:
        # Move back
        backward = (dir + 2) % 4
        x_moved = x_pos + move_x[backward]
        y_moved = y_pos + move_y[backward]
        
        if _map[y_moved][x_moved] != 1:
            x_pos = x_moved
            y_pos = y_moved
            is_possible = True 

# start_print
print(cnt)
# end_print