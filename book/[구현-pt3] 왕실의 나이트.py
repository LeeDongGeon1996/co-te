# solution: 현재 위치에서 움직일 수 있는 모든 방향을 완전 탐색한다.
# time-complexity: O(1) - 상수시간

move_x = [-2, -2, 2, 2, 1, -1, 1, -1]
#move_y = [1, -1, 1, -1, -2, -2, 2, 2]

# start_input
pos = input()
# end_input

# exception
assert pos[0].isalpha()
assert pos[1].isdigit() and 0 < int(pos[1]) and int(pos[1]) < 9

col = ord(pos[0]) - ord('a') + 1 
row = int(pos[1])

cnt = 0
for i in range(len(move_x)):
    to_move_x = col + move_x[i]
    to_move_y = row + move_x[-(i + 1)]
    if to_move_x > 0 and to_move_x < 9 and to_move_y > 0 and to_move_y < 9:
        cnt += 1

# start_print
print(cnt)
# end_print
