# solution: brute-force, 1개로 자르는 경우부터 len(N)/2개로 자르는 경우까지 모두 탐색.
# time-complexity: O(N^2)
# url: https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    N = len(s)
    answer = N
    
    for i in range(1, N//2 + 1):
        compressed = ''
        start_idx = 0
        while i + start_idx < N:
            next_idx = start_idx + i
            recur_str = s[start_idx:next_idx]
            
            is_recur = True
            cnt = 1
            while is_recur:
                is_recur = False
                if s[next_idx:next_idx + i] == recur_str:
                    cnt += 1
                    next_idx += i
                    if next_idx + i <= N:
                        is_recur = True
                
            if cnt > 1:
                start_idx  += i*cnt
                compressed += (str(cnt) + recur_str)
            else:
                compressed += s[start_idx:start_idx+i]
                start_idx += i
                
        compressed += s[start_idx:]
        if answer > len(compressed): answer = len(compressed) 
        
    return answer

