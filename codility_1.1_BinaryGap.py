def solution(n):
    zero_count = 0
    result = 0
    while n != 0 and n % 2 == 0:  # Skipping the tailing zero in a binary representation
        n = n // 2
    while n != 0:
        if n % 2 == 0:
            zero_count += 1
            result = max(zero_count, result)
        else:

            zero_count = 0

        n = n // 2

    return result


print(solution(1041))
