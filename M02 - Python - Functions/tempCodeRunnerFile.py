# Function to calculate whether a number is even or odd.

def even_odd(num):
                 
    if num % 2 == 0:
        print(f'{num} is even.')
    else:
        print(f'{num} is odd.')

num = int(input(f'Please enter a number:'))
even_odd(num)