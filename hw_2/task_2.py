from fractions import Fraction


def getting_numbers(string):
    numerator, denominator = map(int, string.split('/'))
    return numerator, denominator


def sum_fractions(fraction1, fraction2):
    numerator_1, denominator_1 = fraction1
    numerator_2, denominator_2 = fraction2
    result_numerator = numerator_1 * denominator_2 + numerator_2 * denominator_1
    result_denominator = denominator_1 * denominator_2
    return result_numerator, result_denominator


def prod_fractions(fraction1, fraction2):
    numerator1, denominator1 = fraction1
    numerator2, denominator2 = fraction2
    result_numerator = numerator1 * numerator2
    result_denominator = denominator1 * denominator2
    return result_numerator, result_denominator


def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def shorten_the_fraction(fraction):
    numerator, denominator = fraction
    common_divisor = greatest_common_divisor(numerator, denominator)
    reduced_numerator = numerator // common_divisor
    reduced_denominator = denominator // common_divisor
    return reduced_numerator, reduced_denominator


string_1 = input("1. Введите первую дробь в формате a/b: ")
string_2 = input("2. Введите вторую дробь в формате a/b: ")

extracting_number_1 = getting_numbers(string_1)
extracting_number_2 = getting_numbers(string_2)
sum_fractions = sum_fractions(extracting_number_1, extracting_number_2)
reduced_sum_fractions = shorten_the_fraction(sum_fractions)
print("1. Сумма дробей:", '/'.join(map(str, reduced_sum_fractions)))
prod_fractions = prod_fractions(extracting_number_1, extracting_number_2)
reduced_prod_fractions = shorten_the_fraction(prod_fractions)
print("2. Произведение дробей:", '/'.join(map(str, reduced_prod_fractions)))

print(f'1. Проверка результата : {Fraction(string_1) + Fraction(string_2)}')
print(f'2. Проверка результата : {Fraction(string_1) * Fraction(string_2)}')
