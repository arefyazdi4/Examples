if __name__ == '__main__':
    num = int(input())
    student_list = []
    for i in range(num):
        tmp = input().split()
        student_list.append(tmp)
    new_student_list = list()
    for indx, student in enumerate(student_list):
        new_student = [index+1 for index, state in enumerate(student) if state == '0' and indx != index]
        new_student_list.append(new_student)
    student_list = list(enumerate(new_student_list))
    print(student_list)
    student_list.sort(key=lambda n: len(n[1]), reverse=True)
    print(student_list)
