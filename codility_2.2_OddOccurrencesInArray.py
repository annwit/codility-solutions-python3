def solution(A):
    result = 0
    for a in A:
        result ^= a
    return result


# Test
A1 = [9, 3, 9, 3, 9, 7, 9]

print(solution(A1))
