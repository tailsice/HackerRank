if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    target = list(arr)
    res = []
    for i in target:
        if i not in res:
            res.append(i)
    res.sort()
    MaxNumber = max(res)
    res.remove(MaxNumber)
    print(str(max(res)))
