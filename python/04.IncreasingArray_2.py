limit = int(input())
userInput = list(map(int, input().split()))

result = 0

if len(userInput) > 1:
    for index in range(1, len(userInput)):
        diff = userInput[index] - userInput[index-1]
        if diff < 0:
            result += diff
            userInput[index] = userInput[index-1]
            

print(abs(result))
