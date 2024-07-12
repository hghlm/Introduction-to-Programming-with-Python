# Question 1: Classify the following potential non-constant variable names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.
print("Question 1:")
print("index is idiomatic")
print("CatName is non-idiomatic, starts with capital")
print("lazy_dog is idiomatic")
print("quick_Fox is non-idiomatic, capital on Fox")
print("1stCharacter is illegal, starts with number")
print("operand2 is idiomatic")
print("BIG_NUMBER is non-idiomatic, uses all capitals which should be for constants")
print("π is non-idiomatic, not ASCII char")
print()

# Question 2: Classify the following potential function names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.
print("Question 2:")
print('function names same as variable names, same answers')
print()

# Question 3: Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.
print("Question 3:")
print('LAZY_DOG3 and BIG_NUMBER are idiomatic, rest are either non-idiomatic or illegal')
print()

# Question 4: Classify the following potential class names as idiomatic, non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.
print("Question 4:")
print('CatName and BigNumber3 are idiomatic, others are non-idiomatic or illegal, no underscores allowed')
print()

# Question 5: Write a program named greeter.py that greets 'Victor' three times. Your program should use a variable and not hard code the string value 'Victor' in each greeting.
print("Question 5:")
name = "Victor"
print("Good Morning, " + name + ".")
print("Good Afternoon, " + name + ".")
print("Good Evening, " + name + ".")
print()

# Question 6: Write a program named age.py that includes someone's age and then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 22 years old.
print("Question 6:")
age = 22
print("You are " + str(age) + " years old.")
print("In 10 years, you will be " + str(age+10) + " years old.")
print("In 20 years, you will be " + str(age+20) + " years old.")
print("In 30 years, you will be " + str(age+30) + " years old.")
print("In 40 years, you will be " + str(age+40) + " years old.")
print()

# Question 7: What happens when you run the following code? Why?
print("Question 7:")
print("Prints the first 3 strings with Victor and the next 3 with Nina because Python doesn't support constants, should use lower case though if name is a variable that can be changed.")
print()

# Question 8: Math question.
print("Question 8:")
balance = 1000.00 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05
print(balance)
print()

# Question 9: Repeat the previous question but, this time, use augmented assignment to compute the final result, one year at a time.
print("Question 9:")
balance = 1000.00
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
print(balance)
print()

# Question 10: Repeat the previous question but, this time, use augmented assignment to compute the final result, one year at a time.
print("Question 10:")
print("reassigns")
print("neither")
print("reassigns")
print("neither")
print("reassigns")
print("mutates")
print("mutates")
print("mutates")
print("neither")
print("reassigns")



