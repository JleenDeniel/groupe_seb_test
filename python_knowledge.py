"""
№1
На вход подается список lst = [26, 13, 6, 16, 17, 2, 0, 1]

Необходимо разбить список на 2 равные части так, что :
а) если длина списка нечетна, то средний элемент не учитываем
б) если длина списка четна, то учитываем все элементы

Функция должна вернуть True , если сумма первой части списка
больше суммы второй, иначе - вернуть False.

№2
На вход подается список lst = [['Alexey', 23], ['Inna', 26], ['Alex', 39], ['Jane', 37], ['Olga', 42]]

Напишите программу, которая спросит пользователя, что вывести на экран - 
список имен всех членов группы, либо возраст - и выведет запрашиваемое в виде списка : 
а) в алфавитном порядке (если имена)
б) в порядке возрастания (если возраст).

"""

def list_comparing(list: list):
    sum1, sum2 = 0, 0
    if len(list) % 2 != 0:
        list[(len(list) - 1)//2]
        for i in range(0, (len(list) - 1)//2):
            sum1 = sum1 + list[i]
        for j in range((len(list) - 1)//2, len(list)):
            sum2 = sum2 + list[j]
    else:
        for i in range(0, len(list)//2):
            sum1 = sum1 + list[i]
        for j in range(len(list)//2, len(list)):
            sum2 = sum2 + list[j]

    return sum1 > sum2

def people_sorting(list1: list, status: int):
    res = []
    if status == 1:
        for i in range(len(list1)):
            res.append(list1[i][0])
        res = sorted(res)
    if status == 2:
        for i in range(len(list1)):
            res.append(list1[i][1])
        res = sorted(res)
    return res

def main():
    list1 = [26, 13, 6, 16, 17, 200, 1, 10]
    print(list_comparing(list1))
    lst = [['Alexey', 23], ['Inna', 26], ['Alex', 39], ['Jane', 37], ['Olga', 42]]
    print(people_sorting(lst, 2))

main()