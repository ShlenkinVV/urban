grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(students)
dict_ = {}


for i in range(0, len(grades)):
    avg = sum(grades[i]) / len(grades[i])
    name = str(students[i])
    dict_.update({name: avg})

print(dict_)
