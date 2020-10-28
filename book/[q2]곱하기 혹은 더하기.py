# solution: 0만 아니면 무조건 곱을 수행한다.
# fix : 0뿐만 아니라 1인 경우도 덧셈을 하고 / 총합이 1이하인 경우도 뎃셈이 유리.
# time-complexity: O(N)

# start_input
print("입력 : ", end='')
_str = input()
# end_input

result = 0
for j in _str:
        integer = int(j)
        if integer <= 1 or result <= 1:
            result += integer
        else:
            result *= integer

# start_print
print("result : " + str(result))
# end_input