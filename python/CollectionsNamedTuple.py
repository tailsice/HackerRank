# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

if __name__ == "__main__":
    student_num = int(input().strip())
    tuple_fields = input().strip().split()
    
    student = namedtuple('student', tuple_fields)
    library = []
    ans = 0
    
    for _ in range(student_num):
        student_info = input().strip().split()
        library.append(student(student_info[0],student_info[1],student_info[2],student_info[3]))
        
    for el in library:
        ans += int(el.MARKS)
        
    print(ans/student_num)
