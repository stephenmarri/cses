highest = int(input())
nums = [int(i) for i in input().split(" ")]
sum_of_ap = (highest * (highest + 1))//2
print(sum_of_ap - int(sum(nums)))