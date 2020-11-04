# solution: 모든 시각을 완전탐색하여 3의 포함여부 확인.
# time-complexity: O(N) - 선형시간

# start_input
N = int(input())
# end_input

cnt = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1
             
# start_print
print(cnt)
# end_print