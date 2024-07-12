# Question 1: Concatenate two strings, one with your first name and one with your last, to create a new string with your full name as its value.
print("Question 1:")
fullName = "Hugh" + " " + "Lam"
print(fullName)
print()

# Question 2: Use the REPL and the arithmetic operators to extract the individual digits of 4936:
print("Question 2:")
n = 4936

ones = n % 10
tens = (n//10) % 10
hundreds = (n//100) % 10
thousands = n//1000

print("Ones place is " + str(ones))
print("Tens place is " + str(tens))
print("Hundreds place is " + str(hundreds))
print("Thousands place is " + str(thousands))
print()

# Question 3: What does following code do?
print("Question 3:")
print('5' + '10')
print('It prints 510 because it concatenates the strings \'5\' and \'10\' together.')
print()

# Question 4: Refactor the code from the previous exercise to use coercion to print 15 instead.
print("Question 4:")
print(int('5') + int('10'))
print()

# Question 5: Will an error occur if you try to access a list element with an index greater than or equal to the list's length?
print("Question 5:")
print("Yes, there will be an Index error because it is out of range.")
print()

# Question 6:To what value does the following expression evaluate ('foo' == 'Foo')?
print("Question 6:")
print('foo' == 'Foo')
print()

# Question 7: What will the following code do (int('3.1415'))? Why?
print("Question 7:")
print("Prints Value error because the string when converted is not an integer value.")
print()

# Question 8: To what value does the following expression evaluate ('12' < '9')?
print("Question 8:")
print("True because first value of 1 is less than first value of 9. If both were numbers instead of strings, it would print out False.")
print('12' < '9')