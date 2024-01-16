


course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
print(course.find('KEB'))
print(course.rfind('KEB'))
print(course.index('KEB'))
print(course.rindex('KEB'))
print(course.find('Inha'))  # -1
print(course.index('Inha'))  # ValueError: substring not found

print(course)
course = course.replace('KEB', 'Inha', 2)
print(course)
print(course.strip())
print(course.strip("!#.*"))


# print(course)
# print(course.replace('KEB', 'Inha'))
# print(course)
# course = course.replace('KEB', 'Inha')
# print(course)
subjects = "python c++ database linux"
subject = input("수강신청과목 입력 : ")
if subjects.find(subject) != -1:
    print(f"해당 과목이 존재합니다. 위치는 {subjects.find(subject)}번 인덱스입니다.")
else:
    print('해당과목이 존재하지 않습니다')
