# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


patient = int(input("Enter a number: "))
DIVIDER = 16


def conventer(patient):
    res: str = ""
    while patient > 0:
        res = str((patient % DIVIDER)) + res
        patient //= DIVIDER
    return res


print(conventer(patient))
print(hex(patient)[2:])
