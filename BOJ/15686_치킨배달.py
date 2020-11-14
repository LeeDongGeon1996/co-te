# solution: 완전 탐색, M개의 원소를 갖는 조합을 구한후, 각각의 도시치킨거리를 구하고 최솟값을 출력.
# time-complexity: O(N)
# url: https://www.acmicpc.net/problem/15686

# start_input
N, M = map(int, input().split())
_map = []
for _ in range(N):
    _map.append(list(map(int, input().split())))
# end_input

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if _map[i][j] == 1:
            houses.append((i,j))
        elif _map[i][j] == 2:
            chickens.append((i,j))

from itertools import combinations
combination = list(combinations(list(range(len(chickens))), len(chickens) - M))

_min = 10000
for comb in combination:
    city_distance = 0
    for house in houses:
        min_distance = 10000
        for i in range(len(chickens)):
            if i not in comb:
                distance = abs(house[0]-chickens[i][0]) + abs(house[1]-chickens[i][1])
                if min_distance > distance: min_distance = distance

        city_distance += min_distance
    if _min > city_distance: _min = city_distance

# start_print
print(_min)
# end_print