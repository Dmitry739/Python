import math
#1 e^x
dct = {'П': 17, 'Е': 6, 'Т': 20, 'Р': 18, 'О': 16, 'В':3}
for i in dct:
    dct[i] = math.exp(dct[i])
print("словарь с основанием натурального логарифма от букв фамилии ", dct)

dct_sort1 = {}
keys_sort =  sorted(dct, key=dct.get)#сортирует и возращают значения #  в алфавитном порядке №2

for k in keys_sort:
    dct_sort1[k] = dct[k]  # 3) от меньшего к большему
print("словарь отсортированный по ключу ", dct_sort1)

FILE = open('sort_keys.txt', 'w')
FILE.write(str(dct_sort1))
FILE.close()
#от меньшего к большему №3

sort_dict2 = {}
sort_values = sorted(dct.values(), reverse = False) #сортирует и возращают значения

for i in sort_values:
  for j in dct.keys():
    if dct[j]==i:
      sort_dict2 [j]= dct[j]
      break

print("словарь отсортированный по значению  ", sort_dict2)
FILE = open('sort_values.txt', 'w')
FILE.write(str(sort_dict2))
FILE.close()

# №4 генератор словаря

#Функция генератор
dct = {'П': 17, 'Е': 6, 'Т': 20, 'Р': 18, 'О': 16, 'В':3}

def x(n):
    if n == 0:
        return 1
    yield math.exp(n)

for i in dct:
    dct[i] = (next(x(dct[i])))
print("словарь, созданный при помощи генератора", dct)

# №5
list = [] #создаем список и записываем туда все значения
for i in dct:
  list.append(dct[i])
sr = sum(list) / len(list) #среднее арифметическое

list1 = [] # список для < среднего
list2 = [] #список для >= среднего
for i in list: # перебираем значения и записываем их в соответствующий список
  if i < sr: 
    list1.append(i)
  elif i>= sr:
    list2.append(i)

print("список значений меньше среднего ", list1)
print("список значений больше среднего ", list2)

