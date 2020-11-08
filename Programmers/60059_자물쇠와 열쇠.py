# solution: brute-force, 자물쇠를 확장시키고 키를 회전시키며 이동하면서 하나의 경우씩 비교.
# time-complexity: O(N^2)
# url: https://programmers.co.kr/learn/courses/30/lessons/60059

def rotate(ary):
    N = len(ary)
    new_ary = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_ary[j][N-1-i] = ary[i][j]
    
    return new_ary

def check(i, j, expand_size, lock_start, lock_end, key, lock):
    check_ary = [[0]*expand_size for _ in range(expand_size)]
    
    for a in range(len(key)):
        for b in range(len(key)):
            check_ary[i + a][j + b] = key[a][b]
    
    for a in range(lock_start, lock_end):
        for b in range(lock_start, lock_end):
            if check_ary[a][b] + lock[a-lock_start][b-lock_start] != 1:
                return False
            
    return True

def solution(key, lock):
    answer = False
    
    expand_size = len(key)*2 + len(lock) - 2
    lock_start = len(key) - 1
    lock_end = lock_start + len(lock)
    for i in range(4):
        for j in range(lock_end):
            for k in range(lock_end):
                if check(j, k, expand_size, lock_start, lock_end, key, lock):
                    return True
        key = rotate(key)        
        
    return answer
