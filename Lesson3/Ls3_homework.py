#Написать ф-ию factorial, которая принимает число, а возвращает его факториал
def factorial(num):
    #if num < 1:
        #print("В функцию передано число меньше единицы")
        #return 0
    if num == 1:
        return 1
    return num * factorial(num - 1)

print(factorial(3))
print()
for i in range (1, 10):
    print(str(i) + " факториал " + str(factorial(i)))

#Написать декоратор timeit, которые с помощью метода time библиотеки time
# будет выводить вам время исполнения​ ф-ии по её завершению
def timeit(f):
    import time
    def wrap(*args):
        start=time.time()
        f(*args)
        end=time.time()
        print("Время выполнения функции " + str(end - start) + " секунд")
    return wrap

@timeit
def testFunc():
    print("lalala")

testFunc()

@timeit
def testFunc1(a):
    print("gagaga" * a)

testFunc1(5)

@timeit
def testFunc2(n):
    for i in range(0, 100000000):
        n=i;

testFunc2(0)