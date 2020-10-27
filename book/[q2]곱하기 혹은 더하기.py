# solution: 0만 아니면 무조건 곱을 수행한다.
# time-complexity: O(N)

# start_input
print("입력 : ", end='')
_str = input()
# end_input

if int(_str) == 0:
    result = 0
else:    
    result = 1
    for i in _str:
        integer = int(i)
        if integer != 0:
            result *= integer

# start_print
print("result : " + str(result))
# end_input