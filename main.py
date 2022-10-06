num = int(input("Input a number: "))
x = 0

while num > 0:
  if num % 2 == 0:
    num = num/2
  else:
    num -= 1
  x += 1

print(f"Output: {x}")