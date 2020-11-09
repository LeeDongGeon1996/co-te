# solution: 일단 수행해보고, 조건을 만족하지않으면 취소.
#    구조물리스트를 만들어 그들 사이 관계가 조건을 만족하는지 확인한다.
# time-complexity: O(N)
# url: https://programmers.co.kr/learn/courses/30/lessons/60061


# 기둥: 1, 보: 2, 둘다:3 
COL = 1
BO = 2
BOTH = 3

def build_available(map, x, y, type):
    if type == 0:
        if y == 0 or\
        ((y-1>=0)and(map[y][x] == COL or map[y][x] == BOTH)) or\
        (((x-1>=0)and(map[y][x-1] >= BO)) or (map[y][x] >= BO)):
            return True

    else:
        if (map[y-1][x] == COL or map[y-1][x] == BOTH) or\
        (map[y-1][x+1] == COL or map[y-1][x+1] == BOTH) or\
        (((x-1)>=0)and(map[y][x-1] >= BO)and(map[y][x+1] >= BO)):
            return True

    return False

def remove_available(map, x, y, type):
    if type == 0:
        if (map[y+1][x] == COL or map[y+1][x] == BOTH):
            a = 1
            # 조건식 더 작성해야함..
            # 생략

    return False

def solution(n, build_frame):
    answer = []
    
    map = [[0]*n for _ in range(n)]
    
    for cmd in build_frame:
        if cmd[3] == 1 and build_available(map, cmd[0], cmd[1], cmd[2]):
            map[cmd[1]][cmd[0]] += cmd[2] + 1
        elif cmd[3] == 0 and remove_available(map, cmd[0], cmd[1], cmd[2]):
            map[cmd[1]][cmd[0]] -= cmd[2] + 1
    
    for i in range(n):
        for j in range(n):
            if map[j][i] > 2:
                answer.append([i, j, 0])
                answer.append([i, j, 1])
            elif map[j][i] > 1:
                answer.append([i, j, 1])
            elif map[j][i] > 0:
                answer.append([i, j, 0])
    
    return answer