# solution: 0인 구간과 1인 구간중 적은 갯수인 구간을 뒤집는다.
# fix: diff_cnt에서 +1을 한 후, /2 수행.
# time-complexity: O(N) - 선형시간

# start_input
print("입력 : ", end='')
_str = input()
# end_input

diff_cnt = 0
for i in range(len(_str)-1):
    if _str[i] != _str[i+1]:
        diff_cnt += 1

result = int((diff_cnt + 1)/2)

# start_print
print(result)
# end_input