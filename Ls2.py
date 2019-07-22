#Напишите программу, которая выводит на экран числа от 1 до 100.
#При этом вместо чисел, кратных трем, программа должна выводить слово Fizz, а вместо чисел,
#кратных пяти — слово Buzz. Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz.

a=""
for j in range(1, 100):
    if (j % 15) == 0:
        a += "FizzBuzz, "
        #print("FizzBuzz")
    elif (j % 5) == 0:
        a += "Buzz, "
        #print("Buzz")
    elif (j % 3) == 0:
        #print("Fizz")
        a += "Fizz, "
    else:
        #print(j)
        a += str(j)
        a += ", "
a = a[0: -2]
print(a)
print("")


#Циклом получить сумму всех элементов списка
arr = [4, 7, 8, 10, 3]
a=0
for i in arr:
    a += i
print(a)
print("")

#Аналогично, но с использованием другого типа цикла
b=0
count=0
while count < len(arr):
    b += arr[count]
    count += 1
print(b)
print("")

#Написать программу, реализующую теорему Пифагора
a = 3
b = 4
c = ((a ** 2) + (b ** 2)) ** 0.5
print ("Гипотенуза равна {}".format(c))
print("")

#Составить программу, которая будет считывать введённое пятизначное число.
#После чего, каждую цифру этого числа необходимо вывести в новой строке.
num = int(input('Введите пятизначное число : '))
a = 10000
myType = int
for i in range(1, 6):
    tmp = int ((num // a) - ((num // (a * 10)) * 10))
    print ("{} цифра равна {}".format(i, tmp))
    #print (a)
    a /= 10

#сортировка выбором
#найти наименьший элемент в массиве
#поменять местами его и первый элемент в массиве
#найти следующий наименьший элемент в массиве
#и поменять местами его и второй элемент массива
#продолжать это пока весь массив не будет отсортирован
arr = [0, 3, 24, 2, 3, 7]

for i in range(0, len(arr)):
    min = arr[i]
    ind_min = i
    for j in range(i+1, len(arr)):
        if arr[j] < min:
            min = arr[j]
            ind_min = j
    if i != ind_min:
        arr[i], arr[ind_min] = arr[ind_min], arr[i]
print(arr)
