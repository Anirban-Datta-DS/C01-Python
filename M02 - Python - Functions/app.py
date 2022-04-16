# def my_function(a, b, *arg):
#     return a + b

# a = float(input("Enter a number: "))
# b = float(input("Enter another number: "))

# result = "{:.2f}".format(my_function(a, b))

# print(f'Their sum is {result}.')

def adder(*args):
    sum = 0
    for num in args:
        sum += num

    return sum

print(f'Sum is: {adder(1,2,3,4,5)}.')