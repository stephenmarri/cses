def problem(limit):
    if limit in [2,3]: 
       return "NO SOLUTION"
    if limit == 1:
        return 1
    if limit % 2 == 0:
       even_max = limit
       odd_max = limit -1
    else:
       odd_max = limit
       even_max = limit - 1

    even_lst = [i for i in range(2, even_max+1, 2)]
    odd_lst = [i for i in range(1, odd_max+1, 2)]
    
    result = [*even_lst, *odd_lst]
    return " ".join(map(str, result))

   
print(problem(int(input())))