def solution(x):
    f0 = 0
    f1 = 1
    for i in range(x):
        f0, f1 = f0+f1, f0 
    return f0
