import numpy as np
from scipy import stats
from collections import Counter

# arr = [7,5,6,2,7,8,9,3,2,5,6,1,5,5,6,6]
# check = Counter(arr)
# print(check)

# # check[5]=3
# arr.remove(5)
# check = Counter(arr)
# print(check)

dict1 = {5: 3, 7: 2, 4: 1}
print(dict1)
dict1[5] = dict1[5] -1
print(dict1)

# class FreqStack:

#     def __init__(self):
#         self.stack = []
#         self.dict1= defaultdict(int)

#     def push(self, val: int) -> None:
#         self.dict1[val] += 1
#         self.stack.append(val)
#         print(self.dict1)

#     def pop(self) -> int:
#         temp1 = 0
#         temp2 = []
#         # self.stack = self.stack[::-1]
#         # temp = Counter(self.stack)
       
#         max1 = max(self.dict1.values()) 
#         for key,values in self.dict1.items():
#             if values==max1:
#                 temp1 = key
#                 break
#                 #temp2.append(key)
            
#         #temp1 = temp2[0]
#         self.stack.remove(temp1)

#         self.stack = self.stack[::-1]

#         return temp1      
        


# # Your FreqStack object will be instantiated and called as such:
# # obj = FreqStack()
# # obj.push(val)
# # param_2 = obj.pop()





# class FreqStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)

#     def pop(self) -> int:
#         temp1 = 0
#         temp2 = []
#         self.stack = self.stack[::-1]
#         temp = Counter(self.stack)
       
#         max1 = max(temp.values()) 
#         for key,values in temp.items():
#             if values==max1:
#                 temp1 = key
#                 break
#                 #temp2.append(key)
            
#         #temp1 = temp2[0]
#         self.stack.remove(temp1)

#         self.stack = self.stack[::-1]

#         return temp1      
        


# # Your FreqStack object will be instantiated and called as such:
# # obj = FreqStack()
# # obj.push(val)
# # param_2 = obj.pop()





