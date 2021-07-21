# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

if __name__ == "__main__":
    num = int(input().strip())
    deq = deque()
    
    for _ in range(num):
        args = input().strip().split()
        
        if args[0] == 'append':
            deq.append(args[1])
        elif args[0] == 'appendleft':
            deq.appendleft(args[1])
        elif args[0] == 'pop':
            deq.pop()
        elif args[0] == 'popleft':
            deq.popleft()
            
    ans = []
    for i in deq:
        ans.append(i)
        
    print(" ".join(map(str,ans)))
