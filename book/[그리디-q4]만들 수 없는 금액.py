# solution: 조합을 재귀함수로 모두 구했다.(비효율적)
# time-complexity: O(N^N)

# start_input
N = int(input())
coins = list(map(int, input().split()))
# end_input

coins.sort()

def minus(total, idx):
    total -= coins[idx]
    if total > 0:
        return minus(total, idx + 1)
    elif total == 0:
        return True
    else:
        return False

i = 0
is_possible = True
while is_possible:
    is_possible = False
    i += 1
    for idx in range(len(coins)):
        if minus(i, idx):
            is_possible = True
            break

result = i

# start_print
print(result)
# end_print