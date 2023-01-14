# print("hi in quotes")
def centered_average(nums):
  large = nums[0]
  small = nums[0]
  avg = 0
  for i, num in enumerate(nums):
    print(i , num)
    if num > large:
      large = num
    if num < small:
      small = num
    avg += num
    print("avg", avg)
  print("numerator" , avg - large - small)
  print("denominator" , len(nums)-3)
  print("average" , (avg - large - small) / (len(nums)-2))
  return (avg - large - small) / (len(nums)-2)
centered_average([1, 2, 3, 4, 100])
  