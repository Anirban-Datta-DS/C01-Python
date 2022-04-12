def my_function(a, b):
    return a + b

lst = input("Enter two values: ").split()

result = "{:.2f}".format(my_function(float(lst[0]), float(lst[1])))

print(f'Their sum is {result}.')