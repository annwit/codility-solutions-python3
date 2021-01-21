def solution(A):
    n = len(A)
    result = (n + 1) * (n + 2) // 2

    for e in A:
        result -= e

    return result


# def solution(A):
#    n = len(A)
#    return (n + 1) * (n + 2) // 2 - sum(A)
