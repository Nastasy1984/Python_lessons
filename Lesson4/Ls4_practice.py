#Есть класс Person, конструктор которого принимает три параметра (не учитывая self) –
# имя, фамилию и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию, равное единице.

#У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.

#Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер
# …" (вместо троеточия должны выводиться имя и фамилия объекта).

#В основной ветке программы создайте три объекта класса Person. Посмотрите информацию
# о сотрудниках и увольте самое слабое звено.

class Person:

    def __init__(self, first_name, last_name, qualification = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.qualification = qualification

    def __repr__(self):
        return "Employee " + self.first_name + " " + self.last_name + " qualification " + str(self.qualification)

    def __del__(self):
        print('До свидания, мистер {} {}'.format(self.first_name, self.last_name))

my_list = []
my_list.append(Person("Вася", "Иванов", 3))
my_list.append(Person("Коля", "Петров"))
my_list.append(Person("Дима", "Сидоров", 2))

min_qual = my_list[0]
min_qual_ind = 0
for i in range (0, len(my_list)):
    print(my_list[i].__repr__())
    if min_qual.qualification > my_list[i].qualification:
        min_qual = my_list[i]
        min_qual_ind = i
print("")
del (min_qual, my_list[min_qual_ind])

print("")


#Написать класс  Rectangle, который имеет длину и ширину и методы вычисления периметра и площади.
#Создайте класс Square. Он должен иметь такие же методы, что и прямоугольник
#Подумайте над тем, можно ли применить наследование при создании двух этих классов

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_S(self):
        return self.length * self.width

    def calc_perimetr(self):
        return self.length * 2 + self.width * 2

    def __repr__(self):
        return "I am a rectangle with length " + str(self.length) + " and width " + str(self.width)

class Square(Rectangle):
    def __init__(self, side):
        self.length = side
        self.width = side

    def __repr__(self):
        return "I am a square with side " + str(self.length)

my_figures = []
my_figures.append(Rectangle(2,3))
my_figures.append(Square(3))
my_figures.append(Rectangle(2.5,3))
my_figures.append(Square(2.5))

for i in my_figures:
    print(i.__repr__())
    print("S = " +str(i.calc_S()))
    print("perimetr = " + str(i.calc_perimetr()))
    print("")

print("")
