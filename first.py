def line():
    print("-----------------------")


print('Перший варіант')

lst = [[6, 2, 9], [100, 2, 1], [0, 0, 45]]

calculator = 0
total_sum = 0
counter = {}

for row in lst:
    calculator = 0
    for element in row:
        if element == 0:
            calculator += 1
        else:
            continue
    if calculator == 0:
        total_sum += 1
    else:
        continue

print('Сумма рядків у яких немає нульових елементів', total_sum)

for row in lst:
    for element in row:
        element_str = str(element)
        if element_str in counter:
            counter[element_str] += 1
        else:
            counter[element_str] = 1

max_element = 0

for number_lst, x in counter.items():
    if x > 1:
        g = int(number_lst)
        if max_element == 0 or g > max_element:
            max_element = g

if max_element != 1:
    print('Максимальне число яке повторюється більше одного разу', max_element)
else:
    print('Немає максимального числа')

line()

print('Четвертий варіаент')

matr = [[1, 3, 9], [9, 8, 1], [1, 0, 45]]

for col in matr:
    product_number = 1
    contains_negative = False
    for element in col:
        if element < 0:
            contains_negative = True
            break
        else:
            product_number *= element
    if not contains_negative:
        print('добуток елементів у ', col, ' рядку =', product_number)


def sum_paral(matr):
    n = len(matr)
    max_sum = float('-inf')
    for i in range(n):
        current_sum = sum(matr[j][j + i] for j in range(n - i))
        max_sum = max(max_sum, current_sum)

    for i in range(1, n):
        current_sum = sum(matr[j + i][j] for j in range(n - i))
        max_sum = max(max_sum, current_sum)

    return max_sum


max_sum = sum_paral(matr)
print("Максимальная сумма среди элементов диагоналей: ", max_sum)

line()

print('Вісімнадцятий варінт')

total_sum = 0

for row in lst:
    if 0 in row:
        total_sum += 1

print('Сума рядків, що містить хоч один нульовий елемент', total_sum)

