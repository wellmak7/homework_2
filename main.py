                                            ### ЗАДАНИЕ 1 ###

variable = 'text'
my_list = [1, 'two', 5.6, variable]

for i in my_list:
    print(type(i))

                                            ### ЗАДАНИЕ 2 ###

second_list = []

list_size = int(input('Сколько элементов списка будет: '))
print('Поочередно введите элементы списка:')

i = 0
while i < list_size:
    el = input()
    second_list.append(el)
    i += 1

for index in [index for index in range(len(second_list)) if index % 2 == 0]:
    if (index + 1) < len(second_list):
        switched_value = second_list[index]

        second_list[index] = second_list[index + 1]
        second_list[index + 1] = switched_value
    else:
        break

print("Switched list: ", second_list)

                                            ### ЗАДАНИЕ 3 ###

month_num = int(input('Введите номер месяца: '))

months_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', "Лето",
               "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]

months_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето',
               7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}

print('Время года: ', months_list[month_num - 1])
print('Время года: ', months_dict.get(month_num))

                                            ### ЗАДАНИЕ 4 ###

my_str = input('Введите слова через пробел: ')
forth_list = my_str.split()

print("Пронумерованные строки с вашими словами:")

for ind, el in enumerate(forth_list, 1):
    print(ind, el[0:10])

                                            ### ЗАДАНИЕ 5 ###

fifth_list = [7, 5, 3, 3, 2]

new_el = int(input('Введите новый элемент рейтинга: '))

fifth_list.append(new_el)
fifth_list.sort(reverse=True)

print(fifth_list)