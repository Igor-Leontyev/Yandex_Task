# Даны два массива:  
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2] 
# Надо вернуть их пересечение 
# [1, 2, 2, 3] (порядок неважен) 

a = [1, 2, 3, 2, 0]
b = [5, 1, 2, 7, 3, 2] 
res = list()
for i in range(len(a)-1):
    for j in range(len(b)-1):
        if a[i] == b[j]:
            res.append(a[i])
            break
            
print(res)