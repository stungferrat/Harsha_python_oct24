num = int(input("Enter a number: "))

digits = []
while num > 0:
  digits.append(num % 10)
  num //= 10

digits.sort()

if len(digits) < 2:
  print("The number has fewer than 2 digits.")
else:
  print("The second smallest digit is:", digits[1])