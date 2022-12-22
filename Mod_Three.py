def solution(L):
    # Sort the list in descending order
    L.sort(reverse=True)

    # Initialize the result to 0
    result = 0

    # Iterate through the sorted list and check if any combination of the digits is divisible by 3
    for i in range(1, 2 ** len(L)):  # start at 1 to avoid empty combinations
        combination = ""
        for j in range(len(L)):
            if i & (1 << j):
                combination += str(L[j])
        combination = int(combination)
        if combination % 3 == 0:
            result = max(result, combination)

    return result


print(solution([3, 1, 4, 1, 5, 9]))  # should print 94311
print(solution([3, 1, 4, 1]))  # should print 4311
print(solution([1, 2, 3]))  # should print 0
