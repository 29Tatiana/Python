#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
#Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью 
#из википедии или из документации к языку.

text = "Python стал одним из самых популярных языков, он используется в анализе данных,\
машинном обучении, DevOps и веб-разработке, а также в других сферах, включая разработку игр.\
За счёт читабельности, простого синтаксиса и отсутствия необходимости в компиляции язык\
хорошо подходит для обучения программированию, позволяя концентрироваться на изучении\
алгоритмов, концептов и парадигм. Отладка же и экспериментирование в значительной степени\
облегчаются тем фактом, что язык является интерпретируемым. Применяется язык многими \
крупными компаниями, такими как Google или Facebook. По состоянию на сентябрь 2022 года \
Python занимает первое место в рейтинге TIOBE популярности языков программирования с \
показателем 15,74 %. «Языком года» по версии TIOBE Python объявлялся\
в 2007, 2010, 2018, 2020 и 2021 годах."

def most_frequent(text: str) -> list[str]:
    dict_counts = {}
    SHOW_LIMIT = 10
    new_sorted_dictionary = {}
    new_text = text.replace(',', ''). \
        replace('.', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('"', ''). \
        lower(). \
        strip()
    words_list = new_text.split()
    for word in words_list:
        counter = words_list.count(word)
        dict_counts[word] = counter
    sorted_values = sorted(dict_counts.values())[::-1]
    for i in sorted_values:
        for k in dict_counts.keys():
            if dict_counts[k] == i:
                new_sorted_dictionary[k] = dict_counts[k]
    return list(new_sorted_dictionary.items())[0: SHOW_LIMIT]

print(most_frequent(text))