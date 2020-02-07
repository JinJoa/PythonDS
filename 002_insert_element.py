def solution(L, x):
    i = 0
    for i in range(len(L)):
        if x < L[0]:
            L.insert(0, x)
        elif x > L[i]:
            if x < L[i+1]:
                L.insert(i+1, x)

    answer = L
    return answer

assert solution([20, 37, 58, 72, 91], 65)