def solution(A, k):
    n = len(A)
    if n == 0:  # To avoid ZeroDivisionError in line 7 if A is an empty matrix
        return []
    else:
        k = k % n  # In case of k greater than n we want to perform rotation only k%n times
        return A[n - k:n] + A[0:n - k]


# Tests
A1 = [3, 8, 9, 7, 6]
A2 = []
A3 = [0, 0, 0]

print(solution(A1, 3))
print(solution(A2, 3))
print(solution(A3, 3))
