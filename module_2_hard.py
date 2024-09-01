def result(number):
    str_pass = ""
    for i in range(1, number):
        for j in range(1, number):
            if number % (i + j) == 0 and i < j:
                str_pass = str_pass + str(i) + str(j)
    return str_pass
number = int(input("Введите число от 3 до 20 "))
if number < 3 or number > 20:
    print("Вы ввели неверное число")
else:
    print(result(number))