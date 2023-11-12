def add_subtract(x, y):
    print('x + y = ', x+y)
    print('x - y = ', x-y)

def multiply_divide(x, y):
    print('x * y = ', x*y)
    print('x / y = ', x/y)

if __name__ == '__main__':
    print('Enter number x: ')
    x = int(input())
    print('Enter number y: ')
    y = int(input())
    add_subtract(x, y)


