# get number of students n
# for each student input is  >>>  gopi 3 4 5 6
# enter which student average you need in last line
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    count = 0
    for name, scores in student_marks.items():
        if (name == query_name):
            li = student_marks.get(name)
            for j in li:
                sum = sum + j
                count += 1
                average = sum / count
            print("%.2f" %average)



