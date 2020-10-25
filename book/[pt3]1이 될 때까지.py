import time
print("입력 : " , end="")
n, k = map(int, input().split())
start = time.time()

cnt = 0
while n != 1:
    if n < k:
        cnt += n-1
        break

    else:
        cnt += n % k
        
        if n//k > 0:
            cnt += 1
            n //= k


print("Count : " + str(cnt))

end = time.time()

print("Time : " + str(end - start))