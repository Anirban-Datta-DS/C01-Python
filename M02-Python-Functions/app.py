def my_function(a, b):
    return a + b

a = float(input("Enter a number: "))
b = float(input("Enter another number: "))

result = "{:.2f}".format(my_function(a, b))

print(f'Their sum is {result}.')