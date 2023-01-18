# print("hi in quotes")
# def sum13(nums):
#   total = 0
#   prev_13 = False
#   for i in range(len(nums)):
#     print(i)
#     if nums[i] != 13 and not prev_13:
#       print("inside")
#       total += nums[i]
#     elif nums[i] != 13 and prev_13:
#       prev_13 = False
#     else:
#       prev_13 = True
#   return total
    
# output = sum13([1, 2, 2, 1, 13])
# print(output)

# def lone_sum(a, b, c):
#   sum = 0
#   if a != b and a != c: sum += a
#   if b != a and b != c: sum += b
#   if c != a and c != b: sum += c
  
#   return sum
# output = lone_sum(3, 2, 3)
# print(output)

# def lucky_sum(a, b, c):
#   total = 0
#   print("total" , total)
#   if a == 13:
#     total = 0
#   elif b == 13:
#     total = a
#   elif c == 13:
#     total = a + b
#   else:
#     total = a + b + c
#   return total
# output = lucky_sum(1, 2, 3)
# print(output)

def no_teen_sum(a, b, c):
  print("inside no teen sum")
  sum = fix_teen(a)
  sum += fix_teen(b)
  sum += fix_teen(c)
  return sum

def fix_teen(n):

  teen = 0



  print("inside fix teen")
  if n >= 13 and n <= 14 or n <= 17 and n >= 19:
    teen = 0
  else:
    teen = n
  return teen


output = no_teen_sum(2, 13, 1)
print(output)
# print("hi")
# def close_far(a, b, c):
#   print("inside")
#   print(abs(b - a) , abs(c - a) , abs(b - a) , abs(c - a) , (c - b))
#   if abs(b - a) or abs(c - a) <= 1 and abs(b - a) and abs(c - a) and (c - b) >= 2:
#     return True
#   else:
#     return False
# output = close_far(1, 2, 3)
# print(output)