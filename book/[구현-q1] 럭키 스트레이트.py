# solution: 앞에서부터 중간지점까지 뒤에서부터 중간지점까지 더한 후, 값 비교.
# time-complexity: O(N) - 선형시간

# start_input
N = input()
# end_input

front = 0
back = 0
for i in range(len(N)//2):
    front += int(N[i])
    back += int(N[-(i+1)])

result = 'LUCKY' if front == back else 'READY'

# start_print
print(result)
# end_print