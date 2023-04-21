# Sample Input 
# ["eat", "tea", "tan", "ate", "nat", “bat"] 
# Sample Output 
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ] 
# # Т.е. сгруппировать слова по "общим буквам"

# list = ["eat", "tea", "tan", "ate", "nat", "bat"]
# str = ''
# res_list = []

# for i in range(len(list)):
#     for t in range(len(list)):
#         for j in range(len(list[i])):
#             if j in list[t]:
#                 str += j
#         if len(str) == len(list[i]):  
#             res_list.append(str)
         
#         str = ''      


# print(res_list)