num = int(input("Enter a number: "))

last_digit = num % 10

while num >= 10:
  num //= 10

first_digit = num

sum = first_digit + last_digit

print("Sum of first and last digits:", sum)