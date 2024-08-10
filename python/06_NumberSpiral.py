# 06_NumberSpiral.py

def first_half(num: int) -> list:
    lst = []
    for index, i in enumerate(range(1, num + 1)):
        if num % 2 == 0:
            lst.append([i, num])
        else:
            lst.append([num, i])
    return lst


def second_half(num: int) -> list:
    lst = []
    for index, i in enumerate(range(num - 1, 0, -1)):
        if num % 2 == 0:
            lst.append([num, i])
        else:
            lst.append([i, num])
    return lst


def create_seq(num: int) -> list:
    all_sequences = []
    for i in range(1, num + 1):
        result = [*first_half(i), *second_half(i)]
        all_sequences = [*all_sequences, *result]
    return all_sequences


def create_spiral(num: int) -> list:
    sequences = create_seq(num)
    spiral = [[0 for _ in range(num)] for _ in range(num)]

    for index, (a, b) in enumerate(sequences):
        spiral[a - 1][b - 1] = index + 1
    return spiral


def main(a, b):
    sprial = create_spiral(10)   
    print_spiral(sprial) 
    return sprial[b - 1][a - 1]


def print_spiral(lst):
    for i in lst:
        for j in i:
            print(f"{j:<5}", end=" ")
        print("")


if __name__ == "__main__":
    main(1,2)
    exit
    limit = int(input())
    inputs = []
    for i in range(limit):
        current_input = list(map(int, input().split()))
        inputs.append(current_input)
    for a,b in inputs:
        print(main(a, b))
        
