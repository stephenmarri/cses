n = int(input())
result = []

while True:
    result.append(str(n))
    if n == 1:
        break
    if n % 2 == 1:
        n = n*3 + 1
    else:
        n = n//2

print(" ".join(result))
