num = int(input("Enter a number: "))

sum = 0
place = 1

while num > 0:
  digit = num % 10
  if place % 2 == 1 and digit % 2 == 0:
    sum += digit
  place += 1
  num //= 10

print("Sum of odd placed even digits:", sum)