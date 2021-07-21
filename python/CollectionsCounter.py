# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

if __name__ == "__main__":
    num = int(input().strip())
    shoes = list(map(int,input().strip().split()))
    items = int(input().strip())
    ans = 0
    
    store = Counter(shoes)
    for _ in range(items):
        size, money = map(int, input().strip().split(' '))
        
        if store[size] > 0:
            ans += money
            store[size] -= 1
            
    print(ans)
