# # O(n^3) causes time limit exceed


# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         if len(nums)<3:
#             return False
#         stack = [0,0,0]
#         for i in range(len(nums)-2):
#             stack[0]=nums[i]
#             for j in range(i+1,len(nums)-1):                
#                 if nums[j] <= stack[0] or nums[j] == stack[0]:                  
#                     pass
#                 elif nums[j] > stack[0]:
#                     stack[1]= nums[j]
#                     for k in range(j+1,len(nums)):
#                         if nums[k]< stack[1] and nums[k]>stack[0]:
#                             print(stack[0],stack[1],nums[k])      
#                             return True
#                         else:     
#                             pass
            
#         return False