#ф-ию abs(x) - Возвращает абсолютную величину (модуль числа).
def abs(num):
    if num <= 0:
        return -num
    else:
        return num

print(abs(-7))
print(abs(7))
print(abs(-0.7))
print("")
print("Second task")

#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и
# возвращающую True, если оно простое, и False - иначе.
def is_prime(num):
    if not isinstance(num, int):
        return False
    if num <= 1:
        return False
    for i in range (2, (round(num / 2) + 1)):
        if not num % i:
            return False
    return True

#проверка
print("Проверка на диапазоне от -10 до 30")
stroka = ""
for i in range (-10, 30):
    if (is_prime(i)):
        stroka = stroka + str(i) + " "
print(stroka)
print("Проверка на дробном числе")
print (is_prime(2.4))
print("")
print("Third task")


#Написать ф-ию wave, которая будет принимать строку, а возвращать список строк
#с такими же символами, но один из символов будет заглавным

def wave(str):
    list = []
    for i in range(0, len(str)):
        s1 = str[0:i]
        s2 = str[i]
        s3 = str[i+1:len(str)+1]
        tmpStr = s1 + s2.upper() + s3
        list.append(tmpStr)
    return list

print(wave("hello"))
print(wave("vasya"))
print(wave("programmer"))