import numpy as np
import math
import matplotlib.pyplot as plt


# мат. функция f(x)
def f(x):
    return np.power(x,4) - 4 * x - 1

# мат. функция фи от иск
def phi(x):
    return x - (f(x)) /(4 * np.power(x, 3) - 4)

# алгоритм отделения корней
def rootSeparation(x0, x1, deltax):
    x = x0
    y0 = f(x)
    m = 0
    x = x + deltax
    while x <= x1:
        y1 = f(x)
        if y0 * y1 <= 0:
            m = m + 1
            b = x
            a = b - deltax
            print([m, a, b])
        y0 = y1
        x = x +deltax
        y1 = f(x)
    return ''

# алгоритм метода деления пополам
def bisection(a, b, e):
    n = 0
    while (b - a) > e:
        n = n + 1
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    matrix = [n, a]
    return matrix

# алгоритм метода итераций
def iteration(x0, e):
    x = x0
    n = 0
    x1 = phi(x)
    while abs(x1 - x) >= e:
        n = n + 1
        x = x1
        x1 = phi(x)
        matrix = [n + 1, x]
    return matrix

# алгоритм комбинированного метода
def combination(a, b, e):
    n = 0
    while (a - b) > e:
        x = (a + b) / 2
        n = n + 1
        if (abs(f(x)) < abs(f(a))) and (abs(f(x)) < abs(f(b))):
            break
        if f(a) * f(x) <= 0:
            b = x
            n = n + 1
        else:
            a = x
            n = n + 1
    while abs(b - a) > e:
        a = phi(b)
        b = phi(a)
        n = n + 1
    matrix = [n + 1, a]
    return matrix

print("1. Отделение корней")
print()
root = rootSeparation(-10, 10, 0.5)
print(root)

print("2. Метод деления пополам")
print()
print("Интеравал от - 10 до 10")
print(bisection(-10, 10, 0.01))
print(bisection(-10, 10, 0.001))
print(bisection(-10, 10, 0.0001))
print(bisection(-10, 10, 0.00001))
print(bisection(-10, 10, 0.000001))
print()
print("Интервал от -10 до 0")
print(bisection(-10, 0, 0.01))
print(bisection(-10, 0, 0.001))
print(bisection(-10, 0, 0.0001))
print(bisection(-10, 0, 0.00001))
print(bisection(-10, 0, 0.000001))
print()
print("Интервал от 0 до 10")
print(bisection(0, 10, 0.01))
print(bisection(0, 10, 0.001))
print(bisection(0, 10, 0.0001))
print(bisection(0, 10, 0.00001))
print(bisection(0, 10, 0.000001))
print()
print("Интервал от 1.5 до 10")
print(bisection(1.5, 10, 0.01))
print(bisection(1.5, 10, 0.001))
print(bisection(1.5, 10, 0.0001))
print(bisection(1.5, 10, 0.00001))
print(bisection(1.5, 10, 0.000001))
print()
print("Интервал от -0.5 до 0")
print(bisection(-0.5, 0, 0.01))
print(bisection(-0.5, 0, 0.001))
print(bisection(-0.5, 0, 0.0001))
print(bisection(-0.5, 0, 0.00001))
print(bisection(-0.5, 0, 0.000001))
print()
print("Интервал от 1.5 до 2")
print(bisection(1.5, 2, 0.01))
print(bisection(1.5, 2, 0.001))
print(bisection(1.5, 2, 0.0001))
print(bisection(1.5, 2, 0.00001))
print(bisection(1.5, 2, 0.000001))
print()
print("3. Метод итераций")
print()
print("Значение интервала -10")
print(iteration(-10, 0.01))
print(iteration(-10, 0.001))
print(iteration(-10, 0.0001))
print(iteration(-10, 0.00001))
print(iteration(-10, 0.000001))
print()
print("Значение интервала 10")
print(iteration(10, 0.01))
print(iteration(10, 0.001))
print(iteration(10, 0.0001))
print(iteration(10, 0.00001))
print(iteration(10, 0.000001))
print()
print("Значение интервала -0.5")
print(iteration(-0.5, 0.01))
print(iteration(-0.5, 0.001))
print(iteration(-0.5, 0.0001))
print(iteration(-0.5, 0.00001))
print(iteration(-0.5, 0.000001))
print()
print("Значение интервала 0")
print(iteration(0, 0.01))
print(iteration(0, 0.001))
print(iteration(0, 0.0001))
print(iteration(0, 0.00001))
print(iteration(0, 0.000001))
print()
print("Значение интервала 1.5")
print(iteration(1.5, 0.01))
print(iteration(1.5, 0.001))
print(iteration(1.5, 0.0001))
print(iteration(1.5, 0.00001))
print(iteration(1.5, 0.000001))
print()
print("Значение интервала 2")
print(iteration(2, 0.01))
print(iteration(2, 0.001))
print(iteration(2, 0.0001))
print(iteration(2, 0.00001))
print(iteration(2, 0.000001))
print()
print("4. Комбинированный метод")
print()
print("Интеравал от - 10 до 10")
print(combination(-10, 10, 0.01))
print(combination(-10, 10, 0.001))
print(combination(-10, 10, 0.0001))
print(combination(-10, 10, 0.00001))
print(combination(-10, 10, 0.000001))
print()
print("Интервал от -10 до 0")
print(combination(-10, 0, 0.01))
print(combination(-10, 0, 0.001))
print(combination(-10, 0, 0.0001))
print(combination(-10, 0, 0.00001))
print(combination(-10, 0, 0.000001))
print()
print("Интервал от 1.5 до 10")
print(combination(1.5, 10, 0.01))
print(combination(1.5, 10, 0.001))
print(combination(1.5, 10, 0.0001))
print(combination(1.5, 10, 0.00001))
print(combination(1.5, 10, 0.000001))
print()
print("Интервал от -0.5 до 0")
print(combination(-0.5, 0, 0.01))
print(combination(-0.5, 0, 0.001))
print(combination(-0.5, 0, 0.0001))
print(combination(-0.5, 0, 0.00001))
print(combination(-0.5, 0, 0.000001))
print()
print("Интервал от 1.5 до 2")
print(combination(1.5, 2, 0.01))
print(combination(1.5, 2, 0.001))
print(combination(1.5, 2, 0.0001))
print(combination(1.5, 2, 0.00001))
print(combination(1.5, 2, 0.000001))
print()

# график функции на интервале от -10 до 10
def chart1():
    x = np.arange(-10, 10, 0.01)
    y = np.power(x, 4) - 4 * x - 1
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid()
    ax.set_title("График функции на интервале от -10 до 10")
    plt.ylim([-4.5, 10])
    plt.show()

# график функций на малом интервале для 1 корня
def chart2():
    x = np.arange(-0.749, 0.251, 0.01)
    y = np.power(x, 4) - 4 * x - 1
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid()
    ax.set_title("График функций на малом интервале для 1 корня")
    plt.show()

# график функций на малом интервале для 2 корня
def chart3():
    x = np.arange(1.163, 2.163, 0.01)
    y = np.power(x, 4) - 4 * x - 1
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid()
    ax.set_title("График функции на малом интервале для 2 корня")
    plt.show()

# график временных затрат на интервале (-10 ... 0)
def chart4():
    plt.figure()
    plt.title('график временных затрат на интервале (-10 ... 0)')
    plt.xscale('log')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [10, 14, 17, 20, 24], 'r-', label='метод деления пополам')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [11, 11, 11, 12, 12], 'b-', label = 'Метод итераций для а')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [3, 3, 3, 4, 4], 'y-', label = 'Метод итераций для б')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [2, 2, 3, 3, 3], 'g-', label='Комбинированный метод')
    plt.legend(['Деление пополам', 'Итерации для а', 'Итарация для б', 'Комбинированный'])
    plt.grid()
    plt.show()

# график временных затрат на интервале (1.5 ... 10)
def chart5():
    plt.figure()
    plt.xscale('log')
    plt.title("график временных затрат на интервале (1.5 ... 10)")
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [10, 14, 17, 20, 24], 'r-', label='метод деления пополам')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [9, 10, 11, 11, 11], 'y-', label='Метод итераций для а')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [3 , 4, 4, 4, 5], 'b-', label = "Метод итераций для б")
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [6, 6, 7, 7, 7], 'g-', label='Комбинированный метод')
    plt.legend(['Деление пополам', 'Итерации для а', 'Итарация для б', 'Комбинированный'])
    plt.grid()
    plt.show()

# график временных затрат на интервале (-0.5 ... 0)
def chart6():
    plt.figure()
    plt.title("график временных затрат на интервале (-0.5 ... 0)")
    plt.xscale('log')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [6, 9, 13, 16, 19], 'r-', label='метод деления пополам')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [3, 3, 3, 4, 4], 'b-', label='Метод итераций для а')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [2, 2, 3, 3, 3], 'y-', label='Метод итераций для б')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [2, 2, 3, 3, 3], 'g-', label='Комбинированный метод')
    plt.legend(['Деление пополам', 'Итерации для а', 'Итарация для б', 'Комбинированный'])
    plt.grid()
    plt.show()

# график временных затрат на интервале (1.5 ... 2)
def chart7():
    plt.figure()
    plt.xscale('log')
    plt.title("график временных затрат на интервале (1.5 ... 2)")
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [6, 9, 13, 16, 19], 'r-', label='метод деления пополам')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [3, 4, 4, 4, 5], 'b-', label='Метод итераций для а')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [3, 4, 4, 5, 5], 'y-', label='Метод итера  ций для б')
    plt.plot([1e-2, 1e-3, 1e-4, 1e-5, 1e-6], [3, 3, 3, 4, 4], 'g-', label='Комбинированный метод')
    plt.legend(['Деление пополам', 'Итерации для а', 'Итарация для б', 'Комбинированный'])
    plt.grid()
    plt.show()

#chart1()
#chart2()
#chart3()
#chart4()
#chart5()
#chart6()
#chart7()