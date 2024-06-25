limit = int(input())
nums = list(input().split(' '))
nums = [int(i) for i in nums]
num_sum = sum(nums)
sum_of_ap = (limit*(limit+1))//2
print(sum_of_ap - num_sum)
