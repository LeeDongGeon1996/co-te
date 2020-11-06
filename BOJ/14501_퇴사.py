# solution: N번째 job을 선택했을 때, 다음 선택이 될수 있는 job중 최대 cost를 갖는 job을 찾아 cost를 cost_dic에 저장한다.
#   이러한 방식으로 i번째 job이 선택되었을 경우, 최댓값을 갖는 cost를 보장할 수 있다. 
# time-complexity: O(N) - 선형시간
# url: https://www.acmicpc.net/problem/14501

# start_input
N = int(input())
_list = []
for i in range(N):
    _list.append(list(map(int, input().split())))
# end_input

cost_dic = []
cost = 0
for i in range(len(_list)):
    idx = len(_list) - (i+1)
    next_start_idx = idx + _list[idx][0]

    if next_start_idx - 1 > len(_list) -1:
        cost = 0
    elif next_start_idx - 1 == len(_list) -1:
        cost = _list[idx][1]
    else:
        cost = _list[idx][1] + max(cost_dic[:len(_list) - next_start_idx])

    cost_dic.append(cost)
    
result = max(cost_dic)

# start_print
print(result)
# end_print