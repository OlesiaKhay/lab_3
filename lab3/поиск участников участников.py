# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, separator = ','):
    lst1 = set(str1.split(separator))
    lst2 = set(str2.split(separator))
    res = list(lst1 & lst2)
    return sorted(res)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
