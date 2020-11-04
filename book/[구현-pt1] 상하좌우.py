# solution: 상하좌우를 배열로 만들어 순회하며 입력된 경로와 비교한다.
# time-complexity: O(N) - 선형시간
direction = ['L', 'R', 'U', 'D']
move_x = [-1, 1, 0, 0]
move_y = [0, 0, -1, 1]
x_pos = 1
y_pos = 1

# start_input
N = int(input())
path = input().split()
# end_input

for i in path:
    for j in range(len(direction)):
        if i == direction[j]:
            x_moved = x_pos + move_x[j]
            y_moved = y_pos + move_y[j]

    if x_moved < 1 or x_moved > N or y_moved < 1 or y_moved > N:
        continue

    x_pos = x_moved
    y_pos = y_moved

# start_print
print("(" + str(x_pos) + ", " + str(y_pos) + ")")
# end_print