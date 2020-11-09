# solution: brute-force, 주어진 경로 모두 탐색.
# time-complexity: O(N^2)
# url: https://www.acmicpc.net/problem/3190


from collections import deque

N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
dir_changes = deque()
for _ in range(L): dir_changes.append(tuple(input().split())) 

directions = ['R', 'L', 'D', 'U']
move_x = [1, -1, 0, 0]
move_y = [0, 0, 1, -1]

head = (1,1)
snake = deque()
snake.append(head)
direction = 'R'

def convert_dir(direction, LR):
    conv = direction + LR
    if conv == 'RD' or conv == 'LL':
        return 'D'
    if conv == 'RL' or conv == 'LD':
        return 'U'
    if conv == 'UD' or conv == 'DL':
        return 'R'
    if conv == 'UL' or conv == 'DD':
        return 'L'

    return None

def try_move(dir):
    for i in range(len(directions)):
        if dir == directions[i]:
            x_moved = head[1] + move_x[i]
            y_moved = head[0] + move_y[i]

    new_head = (y_moved,x_moved)
    if new_head in snake\
        or x_moved < 1 or x_moved > N\
        or y_moved < 1 or y_moved > N:
        return None
    
    return new_head

time = 0
when_to_change = dir_changes.popleft()
is_alive = True
while is_alive:
    for i in range(time, int(when_to_change[0])):
        new_head = try_move(direction)
        time += 1
        if new_head:
            head = new_head
            snake.append(head)
            if new_head in apples:
                apples.remove(new_head)
            else:
                snake.popleft()
        else:
            is_alive = False
            break

    try:
        direction = convert_dir(direction, when_to_change[1])
        when_to_change = dir_changes.popleft()
    except:
        when_to_change = (101,)

print(time)
