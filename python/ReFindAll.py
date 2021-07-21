# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

if __name__ == "__main__":
    string = input().strip()
    
    Target = 'AEIOUaeiou'
    NonTarget = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
    
    ans = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (NonTarget, Target, NonTarget), string)
    
    print("\n".join(ans or ['-1']))
