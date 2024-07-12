n = 4936

ones = n % 10
tens = (n//10) % 10
hundreds = (n//100) % 10
thousands = n//1000

print("Ones place is " + str(ones))
print("Tens place is " + str(tens))
print("Hundreds place is " + str(hundreds))
print("Thousands place is " + str(thousands))