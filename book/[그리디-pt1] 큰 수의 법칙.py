print("입력 : ", end="")
n, m, k = map(int, input().split())

print("data : ", end="")
data = list(map(int, input().split()))
data.sort()

first = data[n-1]
second = data[n-2]
valid_data = [data[n-1], data[n-2]]

sum = 0
for i in range(m//(k+1)):
    sum += valid_data[0] * k
    sum += valid_data[1]

sum += valid_data[0] * (m%(k+1))

print("Sum : " + str(sum))