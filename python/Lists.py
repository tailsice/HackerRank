if __name__ == '__main__':
    N = int(input())
    
    ans = []
    
    for _ in range(N):
        args = input().strip().split(' ')
        cmd = args[0]
        
        if cmd == 'insert':
            ans.insert(int(args[1]), int(args[2]))
        elif cmd == 'remove':
            ans.remove(int(args[1]))
        elif cmd == 'append':
            ans.append(int(args[1]))
        elif cmd == 'print':
            print(ans)
        elif cmd == 'sort':
            ans.sort()
        elif cmd == 'pop':
            ans.pop()
        elif cmd == 'reverse':
            ans.reverse()
