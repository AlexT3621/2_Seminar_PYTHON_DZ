# ; Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.

# ; Пример:

# ; Для n = 5: сумма = 11,55
n = 5
lst = []
i = 1
sum1 = 0
for i in range(1, 6):
    elm = (1+(1/i))**i
    lst.append(elm)

i += 1
print(lst)
list_length = len(lst)
for i in range(list_length):
    sum1 = sum1+lst[i]
print(sum1)
