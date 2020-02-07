def solution(L, x):
    find = -1
    for i in range(len(L)):
        if x == L[i]:
            find = i
    answer = find
    return answer

