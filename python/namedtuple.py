from collections import namedtuple

studentCount = int(input())
Student = namedtuple('Student', input().split())

totalMarks = 0
for i in range(studentCount):
    st = Student( * input().split() )
    totalMarks += int(st.MARKS)

print('%.2f' % (totalMarks / studentCount))
