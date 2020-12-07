# solution: DFS, 연산자를 하나씩 소비해가며 dfs를 수행하여 모든 순열(?)을 탐색한다.  
# time-complexity: O(|V|+|E|) - V=연산자순열수, E=연산자수(N-1)
# url: https://www.acmicpc.net/problem/14888

# start_input
N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
# end_input

_min = 1000000000
_max = -1000000000

def calc(res, oper, depth):
    if opers[oper] == 0:
        return
    
    global _min, _max

    if oper == 0: res += nums[depth]
    elif oper == 1: res -= nums[depth]
    elif oper == 2: res *= nums[depth]
    else: res = int(res/nums[depth])
    opers[oper] -= 1

    if depth == N-1:
        if _min > res: _min = res
        if _max < res: _max = res
    else:
        for i in range(4): calc(res, i, depth+1)

    opers[oper] += 1

for i in range(4): calc(nums[0], i, 1)

# start_print
print(_max)
print(_min)
# end_print