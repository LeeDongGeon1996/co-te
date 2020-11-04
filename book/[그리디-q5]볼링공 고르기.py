# solution: 중복을 제거한 뒤 카운트한다.
# time-complexity: O(N) - 선형시간

# start_input
N, M = map(int, input().split())
weights = list(map(int, input().split()))
# end_input

cnt = 0
for i in range(len(weights)-1):
    b_weights = weights[i+1:]
    cnt += (len(b_weights) - b_weights.count(weights[i]))

result = cnt

# start_print
print(result)
# end_input