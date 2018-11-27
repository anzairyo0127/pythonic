def reigai(a, b):
    try:
        c = a / b
    except TypeError:
        print('数字を入れて')
    except ZeroDivisionError:
        print('0で割らないで')
    else:
        print('{}でありますな'.format(c))
    finally:
        print('計算終わり')


reigai(1, '2')
