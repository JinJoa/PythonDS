def solution(L, x):
    find = []
    i = 0
    for i in range(len(L)):
        if x == L[i]:
            find.append(i)
    if not find:
        find.append(-1)
    answer = find
    return answer

assert solution([64, 72, 83, 72, 54], 72)