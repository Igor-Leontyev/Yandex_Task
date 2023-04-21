# Дан список интов, повторяющихся
# элементов в списке нет. 
# Нужно преобразовать это множество 
# в строку, сворачивая соседние по числовому
# ряду числа в диапазоны. 
# Примеры: 
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11" 
# [1,4,3,2] => "1-4" 
# [1,4] => "1,4

list_num = [1,4,5,2,3,9,8,12,0,13]
list_num.sort()
str_res = ''

temp = 0
str1 = ''
for i in range(len(list_num)-1):
    if list_num[i+1] - list_num[i] == 1:
        str1 += str(list_num[i])

    elif list_num[i+1] - list_num[i] != 1:
        str1 += str1 +str(list_num[i])
        str_res += str1[0] +'-'+str1[-1]+','
        str1 = ''
    str_res += str1[0] +'-'+str1[-1]
print(list_num[-1])
print(str_res)
        