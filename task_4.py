# Дан массив из нулей и единиц. Нужно определить, 
# какой максимальный по длине подинтервал единиц можно получить, 
# удалив ровно один элемент массива.

arr = [1, 1, 1, 0, 0, 1, 1, 1]
max_len = 0

cur_max_len  = 0
for j in range(len(arr)):
    if arr[j] == 1:
        cur_max_len += 1
    if arr[j] == 0 and arr[j + 1] == 0:
        if(max_len <= cur_max_len):
            max_len = cur_max_len
            print(cur_max_len)
            cur_max_len = 0
    if max_len <= cur_max_len:
        max_len = cur_max_len    
       
    
    
    
print(max_len)
        