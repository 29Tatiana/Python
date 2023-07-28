#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
#Если ключ не хешируем, используйте его строковое представление.



def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result

print(kwargs_to_dict(name='Alex', age=15.5, months=['January', 'February', 'March'],
                     courses={'python': '3.11', 'c#': '2.5'}))