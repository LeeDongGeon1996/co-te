# solution: dfs?, 문제의 순서도를 차례대로 구현하면 의외로 쉽게 풀리는 문제였다.
# time-complexity: O(N)
# url: https://programmers.co.kr/learn/courses/30/lessons/60058


def separate(_str):
    starter = _str[0]
    cnt = 0
    for i in range(len(_str)):
        if _str[i] == starter: cnt += 1
        else: cnt -= 1
        
        if cnt == 0: 
            break
            
    return _str[:i+1], _str[i+1:]

def is_correct(_str):
    cnt = 0
    for i in range(len(_str)):
        if _str[i] == "(": cnt += 1
        else: cnt -= 1
        
        if cnt < 0: 
            return False
        
    return True

def solution(p):
    if not p:
        return p
    
    answer = ''
    v = p
    while v:
        u, v = separate(v)
        if is_correct(u):
            answer += u
        else:
            temp = "("
            temp += solution(v) + ")" 
            u = u[1:len(u)-1]
            for i in u: 
                temp += ("(" if i == ")" else ")")
            
            return answer + temp
         
    return answer

print(solution("(()())()"))