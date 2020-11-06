# solution: 알파벳와 순자를 분리하고 각각을 처리.
# time-complexity: O(N) - 선형시간

# start_input
N = input()
# end_input

alpha_list = []
sum = 0
for i in N:
    if i.isalpha():
        alpha_list.append(i.upper())
    else:
        sum += int(i)
alpha_list.sort()

# start_print
for i in alpha_list: print(i, end='')
print(sum)
# end_print
