main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

# region part.1
dictionary = {}
for symbol in main_str:
    value = dictionary.get(symbol, 0)
    if value == 0:
        dictionary.setdefault(symbol, 1)
    else:
        dictionary[symbol] += 1


# endregion


# region part.2
def get_count_char(str_):
    dictionary_ = {}
    for symbol_ in str_:
        value_ = dictionary_.get(symbol_, 0)
        if value_ == 0:
            dictionary_.setdefault(symbol_, 1)
        else:
            dictionary_[symbol_] += 1
    return dictionary_


# endregion


# region part.3
def get_count_char_lower(str_):
    str_ = str_.lower()
    dictionary_ = {}
    for symbol_ in str_:
        value_ = dictionary_.get(symbol_, 0)
        if value_ == 0:
            dictionary_.setdefault(symbol_, 1)
        else:
            dictionary_[symbol_] += 1
    return dictionary_


# endregion


# region part.4
def get_count_char_isalpha(str_):
    str_ = str_.lower()
    dictionary_ = {}
    for symbol_ in str_:
        value_ = dictionary_.get(symbol_, 0)
        if value_ == 0:
            if symbol_.isalpha():
                dictionary_.setdefault(symbol_, 1)
        else:
            dictionary_[symbol_] += 1
    return dictionary_



# endregion


# region part.5
def get_count_char_percent(str_):
    str_ = str_.lower()
    dictionary_ = {}
    number_of_symbols = 0
    for symbol_ in str_:
        value_ = dictionary_.get(symbol_, 0)
        if value_ == 0:
            if symbol_.isalpha():
                dictionary_.setdefault(symbol_, 1)
                number_of_symbols += 1
        else:
            dictionary_[symbol_] += 1
            number_of_symbols += 1
    print('number_of_symbols =', number_of_symbols)
    for symbol_ in dictionary_:
        dictionary_[symbol_] = '{:f} %'.format(dictionary_[symbol_] * 100 / number_of_symbols)
    return dictionary_


# endregion


# print(dictionary)
# print(get_count_char(main_str))
# print(get_count_char_lower(main_str))
print(get_count_char_isalpha(main_str))
#print(get_count_char_percent(main_str))
