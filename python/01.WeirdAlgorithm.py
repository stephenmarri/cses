num = int(input())
lst = []

while True:
    lst.append(num)
    if num == 1:
        break
    if num % 2 == 0:
        num = num//2
    else: 
        num = (num * 3) + 1

print(*lst)