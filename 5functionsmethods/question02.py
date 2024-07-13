foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

print("It prints out bar because the foo created in the function is local.")