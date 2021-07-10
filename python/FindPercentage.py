#!/usr/bin/python3

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result_len=len(student_marks[query_name])
    offset=0
    total=0

    while offset < result_len:
        total+=student_marks[query_name][offset]
        offset+=1


    print("%.2f" % (total/result_len))

