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

def lucky_sum(a, b, c):
  total = 0
  print("total" , total)
  if a != 13:
    total += a
    print("total a" , total)
  elif b != 13:
    total += b
    print("total b" , total)
  elif c != 13:
    total += c
    print("total c" , total)
  return total
output = lucky_sum(1, 2, 3)
print(output)