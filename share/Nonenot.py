def divide(a, b):
    '''
    第二引数が0の場合は0除算になるため、ValueErrorを返します。
    '''
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


x = 1
y = 0

result = divide(x, y)
if result is None:
    print('Invalid inputs')
else:
    print(result)
