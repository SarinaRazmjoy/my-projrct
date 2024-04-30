from project1 import person
from project1 import person_lessons

list1 = []
list2 = []

while True:
    person2 = person(input("name? "), input("family? "), input(
        "age? "), input("national_code? "), input("start? "))

    person1 = person_lessons(input("riazi? "), input(
        "physics? "), input("olomComputer? "), input("tarikh? "))

    x = person.report_card1(person2)
    y = person_lessons.report_card2(person1)

    list1.append(x)
    list1.append(y)
    list2.append(list1)

    print('------------------')
    f = open("project.txt", "a+")
    f.write(str(x))
    f.write(str(y))
    f.close()

    f = open("project.txt", "r")
    print(f.read())
    print('------------------')

    s = input("continue? ")
    if s == "y":
        list1 = []
        continue
    else:
        break

# print("list2 : ")
# print(list2)

s = input("national_code? ")
c = 0
for i in s:
    for j in list2:
        if c >= len(list2):
            break
        if i in j[0]:
            print(j)
            c += 1
            break