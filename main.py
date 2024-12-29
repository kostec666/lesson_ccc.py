first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Переменная first_result с длинами строк, не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Переменная second_result с парами кортежей одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Переменная third_result с ключ-значение: строка-длина (четная длина)
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Пример вывода
print(first_result)
print(second_result)
print(third_result)