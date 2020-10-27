# solution: 두 수의 차를 5의 배수에 가깝게 만든다.  
# time-complexity: O(1) - 상수시간
# url: https://www.codeup.kr/problem.php?id=3120

# start_input
init, target = map(int, input().split())
# end _input

diff = abs(init-target)
result = diff // 10

diff %= 10
div_5 = diff % 5
if div_5 > 2:
    result += (6 - div_5)
else:
    result += ((diff//5) + div_5)

# start_print
print(result)
# end_print