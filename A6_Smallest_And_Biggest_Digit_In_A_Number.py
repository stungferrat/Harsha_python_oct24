num = int(input("Enter a number: "))

largest_digit = 0
smallest_digit = 9

while num > 0:
  digit = num % 10
  largest_digit = max(largest_digit, digit)
  smallest_digit = min(smallest_digit, digit)
  num //= 10

print("Largest digit:", largest_digit)
print("Smallest digit:", smallest_digit)