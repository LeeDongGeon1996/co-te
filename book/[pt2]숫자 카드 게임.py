print("행/열 : ", end='')
n,m = map(int, input().split())

mat = []
for i in range(n):
    print("Data " + str(i) + "행 : ", end='')
    mat.append(map(int, input().split()))

result = max(map(min, mat))
print("MAX : " + str(result))