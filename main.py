#Просим пользователя ввести число
n = int(input("Введите число n: "))
#Инициализация переменных 
a, b = 0, 1
#Создаём цикл while, который будет выполняться до тех пор, пока значение a меньше или равно введенному пользователем числу n.
while a <= n:
    #Пробел между числами
    print(a, end=' ')
    #Одновременное бновление значений a и b
    a, b = b, a + b 
